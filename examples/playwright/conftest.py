import base64
import os
import pytest
import requests
from playwright.sync_api import sync_playwright
from datetime import datetime

SAUCEDEMO_URL = "https://www.saucedemo.com/"
SAUCE_USERNAME = os.environ.get("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.environ.get("SAUCE_ACCESS_KEY")
SAUCE_BUILD_NAME = "Playwright" + datetime.now().strftime("_%Y%m%d_%H%M%S")

# Update job status on Sauce Labs using requests
def update_job_status(session_id, status):
    url = f"https://api.us-west-1.saucelabs.com/rest/v1/{SAUCE_USERNAME}/jobs/{session_id}"
    auth = base64.b64encode(f"{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json"
    }
    data = {"passed": status == "passed"}
    requests.put(url, headers=headers, json=data)


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def remote_browser(request):
    test_name = request.node.name
    endpoint = "https://ondemand.us-west-1.saucelabs.com/wd/hub/session"
    payload = {
        "capabilities": {
            "alwaysMatch": {
                "platformName": "Windows 11",
                "browserName": "Chrome",
                "sauce:options": {
                    "username": SAUCE_USERNAME,
                    "accessKey": SAUCE_ACCESS_KEY,
                    "devTools": True,
                    "_tptCommanderVersion": "stable",
                    "name": test_name,
                    "build": SAUCE_BUILD_NAME,
                },
                "goog:chromeOptions": {
                    "args": [
                        "--no-sandbox",
                        "--disable-infobars",
                        "--disable-features=SafeBrowsing,PasswordLeakToggleMove",
                    ]
                }
            }
        }
    }
    response = requests.post(endpoint, json=payload, auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY))
    response.raise_for_status()
    session_data = response.json()
    session_id = session_data["value"]["sessionId"]
    delete_endpoint = f"https://ondemand.us-west-1.saucelabs.com/wd/hub/session/{session_id}"
    cdp_endpoint = session_data["value"]["capabilities"].get("se:cdp")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cdp_endpoint)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
        requests.delete(delete_endpoint, auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY))
        sauce_result = "failed" if request.session.testsfailed == 1 else "passed"
        update_job_status(session_id, sauce_result)

