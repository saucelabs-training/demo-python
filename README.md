# Python Selenium Examples
[![CircleCI](https://circleci.com/gh/saucelabs-training/demo-python.svg?style=svg)](https://circleci.com/gh/saucelabs-training/demo-python)

This directory contains example scripts and dependencies for running automated Selenium tests on Sauce Labs using **Python**.You can use these scripts to test your Sauce Labs authentication credentials, setup of your automated testing environment, and try out Sauce Labs features.
> ##### For Demonstration Purposes Only

> The code in these scripts is provided on an "AS-IS” basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. These scripts are provided for educational and demonstration purposes only, and should not be used in production. Issues regarding these scripts should be submitted through GitHub. These scripts are maintained by the Technical Services team at Sauce Labs.

<br />

## Prerequisites

In order to complete these exercises you must complete the following prerequisite installation and configuration steps:

* Install Git
* Install `python` and `pip`
* Install a Test Framework
* (Optional) Install an IDE (PyCharm, Visual Studio Code, Komodo Edit etc.)

Detailed Instructions located in the [prerequisites](prerequisites.md#python-prerequisites) file.
<br />

### Run a Sample Test

1. Navigate to the root project directory and use `pip` to install the latest Selenium library for use in the script:
    ```
    $ pip install -r requirements.txt
    ```
    
2. Run the Test Script
   > In order to run the test on [www.saucelabs.com](www.saucelabs.com), change the values of the **`SAUCE_USERNAME`** and **`SAUCE_ACCESS_KEY`** variables in the test script to your Sauce Username and Sauce Access Key values.
   > To retrieve this information, login to your saucelabs.com account and navigate to **User Settings**;
  
   * Run the following command to test your python script:
        ```
        $ python on-boarding-modules/python-examples/test_module1.py
        ```
        
   * You may also use 'Run Configurations' in your IDE. For directions on how to setup Run/Debug Configurations refer to your IDE Documentation:
        * [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html)
        * [Visual Studio Code Documentation](https://code.visualstudio.com/docs/editor/debugging)
        * [Komodo Edit Documentation](http://docs.komodoide.com/manual)

3. Visit the [saucelabs.com automated build page](https://app.saucelabs.com/dashboard/builds) and select the build `Onboarding Sample App - Python` to see the following test case:
    
    ![2-user-site](2-user-site.png)
    
<br />