# Python Demonstration Scripts - Best Practices

This section demonstrates best practice examples of how to connect and run simple tests using Python on Sauce Labs. As a best practice, we recommend [Pytest](http://pytest.org) as a test framework and runner.

Each suite below (`desktop_web`, `mobile_web`, `mobile_native`) has its own `Pipfile` and its
own `conftest.py`, so dependencies stay scoped to just what that suite needs.

## Quickstart

To run tests, do the following steps:

1. Set your Sauce username and access key as environment variables on the machine you are running tests from as `SAUCE_USERNAME` and `SAUCE_ACCESS_KEY` respectively.
2. `cd` into the suite you want to run, e.g. `cd best_practice/desktop_web`.
3. Run
```
pipenv install
```
4. Run
```
pipenv run best-practice-desktop-us
```
to run against a desktop web app using Sauce Labs' US data center or
```
pipenv run best-practice-desktop-eu
```
to run against the EU data center

## Installation

These tests use Pytest and are configured to run using [Pipenv](https://pipenv.pypa.io/en/latest/). You may use Pytest directly as well. To run these tests, you will need to install

- Python 3.7+ (_NOTE_ these tests are only compatible with Python 3, and have only been tested against Python 3.7+)
- Pipenv

To install dependencies needed for a suite, run
```
pipenv install
```
from inside that suite's directory (`best_practice/desktop_web`, `best_practice/mobile_web`, or
`best_practice/mobile_native`). You can also install Pytest and Selenium/Appium-Python-Client
directly if you do not want to use Pipenv.

Last and certainly not least, set your Sauce username and access key as environment variables on the machine you are running tests from as `SAUCE_USERNAME` and `SAUCE_ACCESS_KEY` respectively.

## Structure of the Best Practice tests

These tests are designed to illustrate how to connect Pytest tests to running on Sauce Labs.

Each suite has its own `conftest.py`, as is conventional with Pytest. That `conftest.py` file
shows how to configure the Webdriver to connect to Sauce Labs via Capabilities.

Each directory contains tests that use fixtures from its own `conftest.py` file. Each directory
contains tests that test against

- desktop web browsers,
- mobile web browsers (on emulators and simulators), and
- a mobile native app on real devices.

All tests make use of the Sauce Demo app, in both [web](https://github.com/saucelabs/sample-app-web) and [native mobile](https://github.com/saucelabs/sample-app-mobile) versions as the app under test.


### Sauce Data Centers

Sauce currently supports multiple data centers, so you can choose where your tests run against. The two data centers provided in these tests are the US-West-1 (US) and EU-Central-1 (EU) data centers.


### US Case

To run desktop web tests, from `best_practice/desktop_web`, run
```
pipenv run best-practice-desktop-us
```
or run
```
pytest -n8 --dc=us .
```
directly if you have Pytest and Selenium installed.

Similarly, from `best_practice/mobile_web`, run
```
pipenv run best-practice-mobile-web-vdc-us
```
or run
```
pytest -n8 --dc=us vdc
```
directly if you have Pytest and Selenium/Appium-Python-Client installed.

To run native mobile app tests against real devices on the Sauce Real Device Cloud (RDC), confirm you have access to real devices on your account, upload the appropriate version of the [sample mobile app](https://github.com/saucelabs/sample-app-mobile/releases) to your account following [this guide](https://wiki.saucelabs.com/display/DOCS/Application+Storage#ApplicationStorage-WhatYou'llNeed).

After this, from `best_practice/mobile_native`, run
```
pipenv run best-practice-mobile-native-us-android
```
for the Android case (or
```
pytest -n8 --dc=us android
```
using Pytest directly) and/or
```
pipenv run best-practice-mobile-native-us-ios
```
for the iOS case (or
```
pytest -n8 --dc=us ios
```
using Pytest directly)

### EU Case

To run desktop web tests, from `best_practice/desktop_web`, run
```
pipenv run best-practice-desktop-eu
```
or run
```
pytest -n8 --dc=eu .
```
directly if you have Pytest and Selenium installed.

Similarly, from `best_practice/mobile_web`, run
```
pipenv run best-practice-mobile-web-vdc-eu
```
or run
```
pytest -n8 --dc=eu vdc
```
directly if you have Pytest and Selenium/Appium-Python-Client installed.

To run native mobile app tests against real devices on the Sauce Real Device Cloud (RDC), confirm you have access to real devices on your account, upload the appropriate version of the [sample mobile app](https://github.com/saucelabs/sample-app-mobile/releases) to your account following [this guide](https://wiki.saucelabs.com/display/DOCS/Application+Storage#ApplicationStorage-WhatYou'llNeed).

After this, from `best_practice/mobile_native`, run
```
pipenv run best-practice-mobile-native-eu-android
```
for the Android case (or
```
pytest -n8 --dc=eu android
```
using Pytest directly) and/or
```
pipenv run best-practice-mobile-native-eu-ios
```
for the iOS case (or
```
pytest -n8 --dc=eu ios
```
using Pytest directly)
