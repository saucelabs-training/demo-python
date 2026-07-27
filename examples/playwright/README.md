# Playwright Examples

This directory contains Playwright test examples for the [Sauce Demo](https://www.saucedemo.com/)
website using Python and pytest (via the [`pytest-playwright`](https://github.com/microsoft/playwright-python)
plugin). Tests run either against a **locally launched browser** (the default) or on **Sauce Labs**
via its native Playwright WebSocket endpoint - switching between them is a single environment
variable, and everything else about the test (browser engine, context/page isolation, native
pytest-playwright flags like `--headed`, `--tracing`, `--screenshot`) behaves identically either way.

## Overview

`TARGET` picks where the browser lives:
- `TARGET` unset or `local` (default): launches a browser on the machine running the tests, via
  Playwright's own `browser_type.launch()`. No Sauce Labs account needed.
- `TARGET=sauce`: connects to Sauce Labs' native Playwright WebSocket endpoint instead - creates a
  native Playwright session on Sauce Labs, connects via `browser_type.connect()` to the returned
  WebSocket endpoint, and reports the test result back to Sauce Labs.

Browser engine selection is **not** a custom environment variable - it's `pytest-playwright`'s own
native `--browser` flag (defaults to `chromium`), so it means the same thing for both targets:
`pytest --browser=firefox` runs Firefox whether you're local or on Sauce. Because only the
`browser` fixture itself is overridden here (not `context`/`page`), every other native
`pytest-playwright` flag also works unchanged for both targets - `--headed`, `--slowmo`,
`--browser-channel`, `--tracing`, `--video`, `--screenshot`, the `browser_context_args` marker,
`skip_browser`/`only_browser` markers, and running multiple engines in one invocation
(`--browser=chromium --browser=firefox`).

`GROUPING` picks how sessions are shared across tests:
- `GROUPING` unset or `module` (default): one session per test **file**, named after the file.
  Every test in that file reuses the same browser/Sauce session in turn.
- `GROUPING=test`: one dedicated, never-shared session per test, named after the test itself.

### Session lifecycle

A session (local browser or Sauce Labs job) is opened for a test and, on teardown, either kept
alive for reuse by the next test in its group (test passed) or closed immediately (test failed) -
so a failing test never leaves a possibly-dirty browser behind for whatever test picks up that
session next. Any sessions still open once the whole run finishes are closed out automatically.
This applies the same way regardless of `TARGET` or `GROUPING`.

## Prerequisites

- Python 3 and `pipenv`
- Playwright browser binaries: `pipenv run playwright install`
- For `TARGET=sauce`: a Sauce Labs account, with `SAUCE_USERNAME` and `SAUCE_ACCESS_KEY`
  environment variables set

## Running Tests

Run all tests locally (default), via the Pipenv script:
```bash
pipenv run playwright-tests
```

Or directly with pytest from the repo root:
```bash
pytest examples/playwright/
```

Run all tests on Sauce Labs:
```bash
TARGET=sauce pytest examples/playwright/
```

Run locally with a specific browser engine (native pytest-playwright flag):
```bash
pytest --browser=firefox examples/playwright/
```

Run with one session per test instead of one per file:
```bash
GROUPING=test pytest examples/playwright/
```

Run headed, with tracing and screenshots on failure (native pytest-playwright flags, work with
either `TARGET`):
```bash
pytest --headed --tracing=on --screenshot=only-on-failure examples/playwright/
```

Run in parallel (the Pipenv script already does this):
```bash
pytest -n8 --dist=loadfile examples/playwright/
```
`--dist=loadfile` is required, not optional, for `GROUPING=module` reuse to actually happen under
`pytest-xdist` - its default scheduling can otherwise split one file's tests across two worker
processes, silently defeating reuse (each worker would open its own separate session for the same
file). `--dist=loadfile` guarantees a file's tests always land on the same worker.

## Viewing Test Results

When `TARGET=sauce`, you can view the results in the [Sauce Labs Dashboard](https://app.saucelabs.com/).
The console output includes a direct link to each job:

```
SauceOnDemandSessionID=<session-id>
Test Job Link: https://app.saucelabs.com/tests/<session-id>
```

## Project Structure

```
examples/playwright/
├── README.md
├── conftest.py        # TARGET/GROUPING logic, overrides the `browser` fixture only
├── test_login.py
└── test_inventory.py
```

## Configuration

| Variable | Default | Description |
|----------|---------|--------------|
| `TARGET` | `local` | Where the browser runs: `local` or `sauce` |
| `GROUPING` | `module` | Session sharing: `module` (one session per test file) or `test` (one per test) |
| `SAUCE_REGION` | `us-west-1` | Data center for all Sauce Labs URLs (e.g. `us-east-1`, `eu-central-1`). Only used when `TARGET=sauce` |
| `SAUCE_BUILD_NAME` | `Playwright Python_<timestamp>` | Build name shown on the Sauce Labs dashboard. Only used when `TARGET=sauce` |
| `SAUCE_USERNAME` / `SAUCE_ACCESS_KEY` | - | Sauce Labs credentials. Only used when `TARGET=sauce` |

Browser engine, headless/headed mode, tracing, video, and screenshots are all controlled by
`pytest-playwright`'s own native flags (`--browser`, `--headed`, `--slowmo`, `--browser-channel`,
`--tracing`, `--video`, `--screenshot`) rather than custom environment variables - see
[`pytest-playwright`'s documentation](https://github.com/microsoft/playwright-python#pytest-plugin)
for the full list.

Note: currently only `platformName: "Linux"` is supported by Sauce Labs' native Playwright
WebSocket endpoint.
