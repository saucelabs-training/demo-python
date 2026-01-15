# Python Demonstration Scripts

This [repository](https://github.com/saucelabs-training/demo-python) contains 
example scripts and dependencies for running automated Selenium tests on Sauce 
Labs using **Python**. You can use these scripts to test your Sauce Labs 
authentication credentials, setup of your automated testing environment, 
and try out Sauce Labs features.

> ###### Disclaimer
>
> The code in these scripts is provided on an "AS-IS" basis without warranty of 
> any kind, either express or implied, including without limitation any implied 
> warranties of condition, uninterrupted use, merchantability, fitness for a 
> particular purpose, or non-infringement. These scripts are provided for 
> educational and demonstration purposes only, and should not be used in 
> production. Issues regarding these scripts should be submitted through GitHub. 
> >
> Some examples in this repository, may require a different account tier beyond 
> free trial. Please contact the [Sauce Labs Sales Team](https://saucelabs.com/contact) for support and 
> information.

## Prerequisites

In order to complete these exercises you must complete the following prerequisite 
installation and configuration steps:

* Install Git
* Install `python` and `pip`
* Install `pipenv` (https://github.com/pypa/pipenv#installation)
* (Optional) Install an IDE (PyCharm, Visual Studio Code, Komodo Edit etc.)

Tested with: Python 3.14. Code targets Python 3; if you use a different Python 
3.x version you may need to update dependencies.

## Running Tests on Sauce Labs

The main purpose of this repository is to show how Sauce Labs works with sample 
Python tests. We have included some samples of using Sauce Labs with some 
common Python test tools. In particular, we have examples using

- Pytest
- robotframework
- Playwright

and these cover using

- Desktop Web browsers on Sauce virtual devices,
- Mobile Web browsers on Sauce emulators/simulators, and
- Real devices to test native mobile apps.

These samples are executed using Pipenv for simplicity. You can find a list of 
available executions in the `Pipfile` under the `[scripts]` section. These 
executions demonstrate how to run tests in parallel on the Sauce Labs.

## Available Pipenv scripts

Below are the scripts defined in `Pipfile` grouped by purpose. Run any of them
with `pipenv run <script-name>`.

- Best-practice (desktop)
  - `best-practice-desktop-us` — runs desktop best-practice tests against the US data center
  - `best-practice-desktop-eu` — runs desktop best-practice tests against the EU data center

- Best-practice (mobile web)
  - `best-practice-mobile-web-vdc-us` — runs mobile web tests on virtual devices (VDC) in US
  - `best-practice-mobile-web-vdc-eu` — runs mobile web tests on virtual devices (VDC) in EU
  - `best-practice-mobile-web-rdc-us` — runs mobile web tests on real devices (RDC) in US
  - `best-practice-mobile-web-rdc-eu` — runs mobile web tests on real devices (RDC) in EU

- Best-practice (mobile native)
  - `best-practice-mobile-native-us-android` — runs native Android tests in US
  - `best-practice-mobile-native-eu-android` — runs native Android tests in EU
  - `best-practice-mobile-native-us-ios` — runs native iOS tests in US
  - `best-practice-mobile-native-eu-ios` — runs native iOS tests in EU

- Examples & demos
  - `demo` — runs the Selenium examples
  - `playwright-tests` — runs the Playwright examples

- Robotframework multi-run scripts (Pabot)
  - `robot-desktop-web-us` — runs desktop web robot tests against US datacenter
  - `robot-desktop-web-eu` — runs desktop web robot tests against EU datacenter
  - `robot-android-us` — runs native Android robot tests against US datacenter
  - `robot-android-eu` — runs native Android robot tests against EU datacenter
  - `robot-ios-us` — runs native iOS robot tests against US datacenter
  - `robot-ios-eu` — runs native iOS robot tests against EU datacenter

Notes:
- VDC = virtual device cloud (emulator/simulator). Use the `vdc` scripts for
  emulator-based testing. RDC = real device cloud (real devices) — use the `rdc` scripts for real-device runs.
- The `--dc` argument used in pytest scripts sets the Sauce Labs data center (us/eu) and is consumed by the tests via fixtures.
- Some robotframework scripts use `pabot` and pass `DATA_CENTER` variables so the tests point to the correct Sauce endpoint.

This repository is divided into two main sections: `best_practice` and `examples`.

We also recommend Pytest overall as a Python test framework and runner.

## Contributing

Pull requests are welcome! If you see something you'd like to add, please 
open a PR. This could include

- more test cases,
- using a particular Sauce feature that is not seen here,
- bugfixes, or
- anything else that looks like it belongs