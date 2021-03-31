# Python Demonstration Scripts
[![CircleCI](https://circleci.com/gh/saucelabs-training/demo-python.svg?style=svg)](https://circleci.com/gh/saucelabs-training/demo-python)

This [repository](https://github.com/saucelabs-training/demo-python) contains example scripts and dependencies for running automated Selenium tests on Sauce Labs using **Python**. You can use these scripts to test your Sauce Labs authentication credentials, setup of your automated testing environment, and try out Sauce Labs features.

> ###### Disclaimer
>
> The code in these scripts is provided on an "AS-IS" basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. These scripts are provided for educational and demonstration purposes only, and should not be used in production. Issues regarding these scripts should be submitted through GitHub. These scripts are maintained by the Technical Services team at Sauce Labs.
>
> Some examples in this repository, may require a different account tier beyond free trial. Please contact the [Sauce Labs Sales Team](https://saucelabs.com/contact) for support and information.

## Prerequisites

In order to complete these exercises you must complete the following prerequisite installation and configuration steps:

* Install Git
* Install `python` and `pip`
* Install `pipenv` (https://github.com/pypa/pipenv#installation)
* (Optional) Install an IDE (PyCharm, Visual Studio Code, Komodo Edit etc.)

**NOTE*: All code here is written in Python 3, and is not guaranteed to work with Python 2. Since Python 2.x is now EOL, it is strongly, **strongly* recommended you either migrate to Python 3.5+ if you are using Python 2, or get started using Python 3.5+. 

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

## Running Tests on Sauce Labs

The main purpose of this repository is to show how Sauce Labs works with sample Python tests. We have included some samples of using Sauce Labs with some common Python test tools. In particular, we have examples using

- Pytest
- Robotframework

and these cover using

- Desktop Web browsers on Sauce virtual devices,
- Mobile Web browsers on Sauce emulators/simulators, and
- Real devices to test native mobile apps.

These samples are executed using Pipenv for simplicity. You can find a list of available executions in the Pipfile for executing tests written in the test tools. These executions demonstrate how to run tests in parallel on the various Sauce Labs platforms.

This repository is divided into two main sections: `best_practices` and `examples`. 

### Best Practices

The `best_practices` directory contains samples of Python tests against desktop web applications, mobile web applications and native mobile applications. Please look in the respective directories to see tests, and look at the `conftest.py` to find the Pytest fixtures. 

We also recommend Pytest overall as a Python test framework and runner.

To run the best practices examples, use Pipenv to run the script of choice. The options are

```
pipenv run best-practice-desktop-us
pipenv run best-practice-desktop-eu
pipenv run best-practice-mobile-web-us
pipenv run best-practice-mobile-web-eu
pipenv run best-practice-mobile-native-us-android
pipenv run best-practice-mobile-native-eu-android
pipenv run best-practice-mobile-native-us-ios
pipenv run best-practice-mobile-native-eu-ios
```

### Examples

The `examples` directory contains examples of various Sauce features and products, such as 

- Sauce Headless `pipenv run headless`, 
- Sauce Visual `pipenv run sauce_visual`,
- Legacy TestObject mobile tests,
- Using W3C Capabilities, and
- Sauce Bindings (Python) `saucebindings-pytest` or `saucebindings-robot`

as well as examples of tests using Sauce with Robotframework.

## Contributing

Naturally, pull requests are welcome! If you see something you'd like to add, please open a PR. This could include

- more test cases,
- using a particular Sauce feature that is not seen here,
- bugfixes, or
- anything else that looks like it belongs