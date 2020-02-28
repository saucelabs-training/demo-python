# Python Demonstration Scripts
[![CircleCI](https://circleci.com/gh/saucelabs-training/demo-python.svg?style=svg)](https://circleci.com/gh/saucelabs-training/demo-python)

This [repository](https://github.com/saucelabs-training/demo-python) contains example scripts and dependencies for running automated Selenium tests on Sauce Labs using **Python**. You can use these scripts to test your Sauce Labs authentication credentials, setup of your automated testing environment, and try out Sauce Labs features.

> ###### Disclaimer
>
> The code in these scripts is provided on an "AS-IS" basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. These scripts are provided for educational and demonstration purposes only, and should not be used in production. Issues regarding these scripts should be submitted through GitHub. These scripts are maintained by the Technical Services team at Sauce Labs.
>
> Some examples in this repository, such as `appium-examples` and `headless-examples`, may require a different account tier beyond free trial. Please contact the [Sauce Labs Sales Team](https://saucelabs.com/contact) for support and information.

<br />

## Solution Outline
* [Tests that can help you quickly and easily get started with Sauce Labs](https://github.com/saucelabs-training/demo-python/tree/master/on-boarding-modules)
* [Tests that use the Headless feature of Sauce Labs](https://github.com/saucelabs-training/demo-python/tree/master/headless-examples) (not included with basic tier or free trial customers)
* [Web Examples using Selenium on Sauce Labs](https://github.com/saucelabs-training/demo-python/tree/master/selenium-examples/)
* [Mobile Examples using Appium on Sauce Labs](https://github.com/saucelabs-training/demo-python/tree/master/appium-examples/)

<br />

## Prerequisites

In order to complete these exercises you must complete the following prerequisite installation and configuration steps:

* Install Git
* Install `python` and `pip`
* Install `pipenv` (https://github.com/pypa/pipenv#installation)
* Install a Test Framework
* (Optional) Install an IDE (PyCharm, Visual Studio Code, Komodo Edit etc.)

Detailed Instructions located in the [prerequisites](prerequisites.md#python-prerequisites) file.

**NOTE*: All code here is written in Python 3, and is not guaranteed to work with Python 2. It is strongly, strongly recommended you either migrate to Python 3.5+ if you are using Python 2, or get started using Python 3.5+. 

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

<br />
    
### Run the Onboarding Scripts

If you would like to get started with using Python and Sauce Labs with some guidance, please look at the Onboarding scripts provided in the [`on-boarding-modules`](https://github.com/saucelabs-training/demo-python/on-boarding-modules/README.md) directory.

<br />

### Run the Sauce Examples

In addition to onboarding, we have also included some samples of using Sauce Labs with some common Python test tools. In particular, we have examples using

- Pytest
- Robotframework

and these cover using

- Sauce Labs Virtual Device Cloud (VDC), which includes desktop browsers and  emulator/simulator devices (EMUSIM)
- Sauce Labs Real Device Cloud (RDC).

These samples are executed using Pipenv for simplicity. You can find a list of available executions in the Pipfile for executing tests written in the test tools. These executions demonstrate how to run tests in parallel on the various Sauce Labs platforms.

The organization of these samples are as follows:

-- driver (appium or selenium) 
   |- test tooling
      |- test environment (virtual or real devices)
         |- additional resources needed (if any)
            |- sample test framework