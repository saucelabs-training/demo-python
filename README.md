# Python Demonstration Scripts
[![CircleCI](https://circleci.com/gh/saucelabs-training/demo-python.svg?style=svg)](https://circleci.com/gh/saucelabs-training/demo-python)

**TL;DR** This [repository](https://github.com/saucelabs-training/demo-python) contains example scripts and dependencies for running automated tests on Sauce Labs using **Python**. You can run these scripts to test your Sauce Labs authentication credentials, setup of your automated testing environment, and try out Sauce Labs features, or just read them for some good example of Selenium and Appium tests in Python!


> Some examples in this repository, may require a different account tier beyond free trial. Please contact the [Sauce Labs Sales Team](https://saucelabs.com/contact) for support and information.

## Prerequisites

In order to run these examples you must install and have the following:

* Install Git
* Install `python` and `pip`
* A Sauce Labs account with your Sauce Labs username and access key [set as environment variables](https://docs.saucelabs.com/basics/environment-variables/).

Optional  (Choose your own adventure!)
* For Pipenv - Install pipenv [fromm here](https://github.com/pypa/pipenv#installation)
* For Poetry - Install poetry [from here](https://python-poetry.org/docs/#installation)
* For IDE usage - Install an IDE (PyCharm and Visual Studio Code are generally good)

**NOTE*: All code here is written in Python 3, and is not guaranteed to work with Python 2. Since Python 2.x is now EOL, it is strongly, **strongly* recommended you either migrate to Python 3.7+ if you are using Python 2, or get started using Python 3.7+. 

>   #### Try Demo in Gitpod
>   Select the button below to try this demo in [Gitpod](https://www.gitpod.io/)
>
>  [![Open in Gitpod](open-in-gitpod.png)](https://gitpod.io/#https://github.com/saucelabs-training/demo-python)
>
>   After the gitpod session launches, navigate to the terminal and run the following commands to save your [Sauce Labs Credentials](https://app.saucelabs.com/user-settings) to gitpod as environment variables:
>   ```
>   eval $(gp env -e SAUCE_USERNAME=******)
>   eval $(gp env -e SAUCE_ACCESS_KEY=******)
>   ```
>   Click the following link if you're unsure how to [access your Sauce Labs credentials.](https://wiki.saucelabs.com/display/DOCS/Best+Practice%3A+Use+Environment+Variables+for+Authentication+Credentials)
>   Also, if you start a new terminal in gitpod, you have to run the following command to reset envrionment variables:
>   ```
>   eval $(gp env -e)
>   ```
>  
>   For more information consult the [gitpod documentation](https://www.gitpod.io/docs/47_environment_variables/)

## Installation

To install the needed dependencies for these test examples, you can use Poetry (recommended), Pipenv or Pip. The test scripts should execute exactly the same regardless of which packaging tool you use.  _Please_ only use one of these approaches unless you absolutely know what you're doing.

### Poetry

Run

```bash
poetry install
```

### Pipenv

Run
```bash
pipenv install
```

### Pip

```bash
pip install -r requirements.txt
```
Using a virtual environment is recommended but not required.

## Running Tests on Sauce Labs

The main purpose of this repository is to show how Sauce Labs works with sample Python tests. We have included some samples of using Sauce Labs with some common Python test tools. In particular, we have examples using

- Pytest
- Robotframework

and these cover using

- Desktop Web browsers on Sauce virtual devices,
- Mobile Web browsers on Sauce emulators/simulators, and
- Real devices to test native mobile apps.

This repository is divided into two main sections: `best_practices` and `examples`. 

### Best Practices

The `best_practices` directory contains samples of Python tests against desktop web applications, mobile web applications and native mobile applications. Please look in the respective directories to see tests, and look at the `conftest.py` to find the Pytest fixtures. 

We also recommend Pytest overall as a Python test framework and runner.

### Running using Poetry

To run best practices examples for desktop web applications using Selenium, run
```bash
poetry run pytest best_practices/desktop_web # set --dc to eu or apac for other data centers
```

To run best practices examples for mobile web applications using Selenium, run
```bash
poetry run pytest best_practices/mobile_web/vdc # set --dc to eu or apac for other data centers
```

To run best practices examples for native mobile applications using Appium, run
```bash
poetry run pytest best_practices/native_mobile # set --dc to eu or apac for other data centers
```

### Running using Pipenv

To run best practices examples for desktop web applications using Selenium, run
```bash
pipenv run best-practice-desktop-us # us data center case
pipenv run best-practice-desktop-eu # us data center case
```

To run best practices examples for mobile web applications using Selenium, run
```bash
pipenv run best-practice-mobile-web-vdc-us # us data center case
pipenv run best-practice-mobile-web-vdc-eu  # eu data center case
```

To run best practices examples for native mobile applications using Appium, run
```bash
pipenv run best-practice-mobile-native-us-android # us data center case for Android
pipenv run best-practice-mobile-native-us-ios # us data center case for iOS
pipenv run best-practice-mobile-native-eu-android # eu data center case for Android
pipenv run best-practice-mobile-native-eu-ios # eu data center case for iOS
```

### Running using Pip and Pytest directly

To run best practices examples for desktop web applications using Selenium, run
```bash
pytest best_practices/desktop_web # set --dc to eu or apac for other data centers
```

To run best practices examples for mobile web applications using Selenium, run
```bash
pytest best_practices/mobile_web/vdc # set --dc to eu or apac for other data centers
```

To run best practices examples for native mobile applications using Appium, run
```bash
pytest best_practices/native_mobile # set --dc to eu or apac for other data centers
```


### Examples

The `examples` directory contains examples of various Sauce features and products, such as 

- Sauce Headless 
- Sauce Visual 
- Using W3C Capabilities, and
- Sauce Bindings (Python) `saucebindings-pytest` or `saucebindings-robot`

as well as examples of tests using [Sauce with Robotframework](./examples/robotframework/README.md).

## Contributing

Naturally, pull requests are welcome! If you see something you'd like to add, please open a PR. This could include

- more test cases,
- using a particular Sauce feature that is not seen here,
- bugfixes, or
- anything else that looks like it belongs