import base64
import importlib.metadata
import os
from datetime import datetime

import pytest
import requests

SAUCE_DEMO_URL = "https://www.saucedemo.com/"

SAUCE_USERNAME = os.environ.get("SAUCE_USERNAME", "")
SAUCE_ACCESS_KEY = os.environ.get("SAUCE_ACCESS_KEY", "")
SAUCE_REGION = os.environ.get("SAUCE_REGION", "us-west-1")
SAUCE_URL = f"https://ondemand.{SAUCE_REGION}.saucelabs.com"
SAUCE_API_URL = f"https://api.{SAUCE_REGION}.saucelabs.com"
SAUCE_BUILD_NAME = os.environ.get(
    "SAUCE_BUILD_NAME", "Playwright Python" + datetime.now().strftime("_%Y%m%d_%H%M%S")
)

# TARGET selects whether a session is a locally launched browser or a Sauce Labs one - anything
# other than "sauce" defaults to local, mirroring the C#/JS ports. Browser engine selection is
# NOT our own env var - it's pytest-playwright's native `--browser` flag (browser_type fixture
# below), so `--headed`, `--slowmo`, `--browser-channel` etc. all apply the same way regardless
# of TARGET.
TARGET = os.environ.get("TARGET", "local").strip().lower()

# GROUPING picks how sessions are shared across tests - anything other than "test" defaults to
# "module" (one session per test file, named after the file), the natural Python equivalent of the
# C# port's per-class grouping: pytest test files here are plain functions, not classes, so the
# file is the closest analog to demo-js's own spec-file (`groupBySpec`) grouping unit.
# "test": one dedicated, never-shared session per test, named after the test itself.
GROUPING = os.environ.get("GROUPING", "module").strip().lower()


def _playwright_version():
    # importlib.metadata reads the actually-installed package version (matches `pip show
    # playwright`) rather than an attribute baked into the package at build time - verified
    # empirically, since the equivalent lookup silently returned a stale value in the C# port.
    version = importlib.metadata.version("playwright")
    major, minor = version.split(".")[:2]
    return f"{major}.{minor}"


PLAYWRIGHT_VERSION = _playwright_version()


class WorkerSession:
    def __init__(self, browser, session_id=None):
        self.browser = browser
        self.session_id = session_id


# "module" mode only: one entry per (test module, browser engine), holding that combination's
# shared session - keyed on browser engine too since --browser can be passed more than once to
# parametrize a single run across engines. Plain dict is safe without locking because pytest runs
# tests within one worker process sequentially - unlike the C# port's NUnit fixtures, which run
# truly in parallel via threads and need a ConcurrentDictionary. Under pytest-xdist each worker is
# a separate process with its own copy of this dict, so reuse only happens for tests that land on
# the same worker (see the "playwright-tests" Pipfile script, which uses --dist=loadfile to
# guarantee that for same-module tests).
_module_sessions = {}


def _build_capabilities_payload(session_name, browser_name):
    return {
        "browserName": browser_name,
        "platformName": "Linux",
        "playwrightVersion": PLAYWRIGHT_VERSION,
        "sauce:options": {
            "name": session_name,
            "build": SAUCE_BUILD_NAME,
        },
    }


def _open_sauce_session(browser_type, session_name):
    browser_name = browser_type.name
    auth = (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
    # The endpoint 303-redirects while the VM spins up; follow until we get a 200.
    response = requests.post(
        f"{SAUCE_URL}/playwright/session",
        json=_build_capabilities_payload(session_name, browser_name),
        auth=auth,
        allow_redirects=False,
        timeout=120,
    )
    while response.status_code == 303:
        location = response.headers.get("location")
        if not location:
            raise RuntimeError(
                f"Sauce responded {response.status_code} to POST /playwright/session "
                "without a Location header."
            )
        if not location.startswith("http"):
            location = f"{SAUCE_URL}/{location.lstrip('/')}"
        response = requests.get(location, auth=auth, allow_redirects=False, timeout=120)

    response.raise_for_status()
    body = response.json()
    value = body.get("value", body)
    session_id = value["sessionId"]
    ws_endpoint = value["wsEndpoint"]

    browser = browser_type.connect(f"{ws_endpoint}?browser={browser_name}")
    return WorkerSession(browser, session_id)


def _open_local_session(browser_type, launch_args):
    # Native launch_browser (pytest_playwright.py) does the same launch(**launch_args) call - this
    # is what makes --headed/--slowmo/--browser-channel apply here exactly as they would natively.
    browser = browser_type.launch(**launch_args)
    return WorkerSession(browser)


def _open_session(browser_type, launch_args, session_name):
    if TARGET == "sauce":
        return _open_sauce_session(browser_type, session_name)
    return _open_local_session(browser_type, launch_args)


def _update_sauce_result(session_id, passed):
    url = f"{SAUCE_API_URL}/rest/v1/{SAUCE_USERNAME}/jobs/{session_id}"
    auth = base64.b64encode(f"{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}
    requests.put(url, headers=headers, json={"passed": passed}, timeout=30)


def _close_session(session, passed):
    try:
        if session.session_id:
            _update_sauce_result(session.session_id, passed)
            print(f"SauceOnDemandSessionID={session.session_id}")
            print(f"Test Job Link: https://app.saucelabs.com/tests/{session.session_id}")
        # The Sauce session ends when its WebSocket connection drops; a local browser just closes.
        session.browser.close()
    except Exception as exc:
        print(f"Error closing session {session.session_id}: {exc}")


def _test_passed(request):
    report = getattr(request.node, "rep_call", None)
    return bool(report and report.passed)


@pytest.fixture
def browser(request, browser_type, browser_type_launch_args):
    # Overrides pytest-playwright's own `browser` fixture. Everything above it in the native chain
    # (new_context/context/page, browser_context_args marker, --screenshot/--video/--tracing
    # artifacts) is untouched and works against this Browser exactly as it would against a locally
    # launched one - only *how* the Browser is obtained changes with TARGET. This has to stay
    # function-scoped (not module-scoped) regardless of GROUPING: module-scoped teardown only runs
    # once, at the very end of the module, which can't express "evict immediately on failure" -
    # that needs to be checked after every single test.
    browser_name = browser_type.name

    if GROUPING == "test":
        session = _open_session(browser_type, browser_type_launch_args, request.node.name)
    else:
        module_name = request.module.__name__.rsplit(".", 1)[-1]
        cache_key = (module_name, browser_name)
        session = _module_sessions.get(cache_key)
        if session is None:
            session = _open_session(browser_type, browser_type_launch_args, module_name)
            _module_sessions[cache_key] = session

    yield session.browser

    passed = _test_passed(request)

    if GROUPING == "test":
        # Never shared, so there's nobody to hand this off to - always close and report, pass or fail.
        _close_session(session, passed)
    elif not passed:
        # Passed: leave the session for the next test in this module to reuse. Failed: evict and
        # close it now instead of leaving a possibly-dirty browser for the next test to inherit.
        _module_sessions.pop((module_name, browser_name), None)
        _close_session(session, passed=False)


@pytest.fixture(scope="session", autouse=True)
def _close_leftover_module_sessions(playwright):
    # Depending on `playwright` (native, session-scoped) isn't for its value - it's what makes
    # pytest tear this fixture down *before* the driver itself stops (fixture teardown is LIFO by
    # setup order). Without that dependency this ran after the driver had already stopped, and
    # browser.close() failed with "Event loop is closed" - confirmed empirically.
    yield
    # Closes every session still in _module_sessions ("test" mode never populates it - each session
    # is already closed in the browser fixture). Any module session that ever failed a test was
    # already evicted and closed there, so everything left here only ever ran passing tests.
    for module_session in _module_sessions.values():
        _close_session(module_session, passed=True)
    _module_sessions.clear()
