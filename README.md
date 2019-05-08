# Python Selenium Examples
[![CircleCI](https://circleci.com/gh/saucelabs-training/demo-python.svg?style=svg)](https://circleci.com/gh/saucelabs-training/demo-python)

This directory contains example scripts and dependencies for running automated Selenium tests on Sauce Labs using **Python**. You can use these scripts to test your Sauce Labs authentication credentials, the setup of your automated testing environment, and try out Sauce Labs features, like cross-browser testing. Feel free to copy these files or clone the entire directory to your local environment to experiment with creating your own automated Selenium tests!

#### For Demonstration Purposes Only

The code in these scripts is provided on an "AS-IS” basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. These scripts are provided for educational and demonstration purposes only, and should not be used in production. Issues regarding these scripts should be submitted through GitHub. These scripts are maintained by the Technical Services team at Sauce Labs.

<br />

## Description

These procedures will show you to set up a Selenium environment for Python. The scripts in this repository allow you run a simple automated test to validate your Selenium environment and your [saucelabs.com](https://app.saucelabs.com/login) account credentials.

<br />

## Prerequisites

In order to complete these exercises you must complete the following prerequisite installation and configuration steps:

* Install Git
* Install `python` and `pip`
* Install an IDE (PyCharm, Visual Studio Code, Komodo Edit etc.)
* Setup Project

### Install Git

[Git](https://git-scm.com/doc) is a version control system that lets you check out code from a repository, 
work with that code on your own branch, and then merge that code with any changes that have been made by other developers. 
Git is an essential tool for distributed development teams, and is a critical component of the continuous 
integration/continuous development toolchain.

##### MacOSX:

1. Go to [https://git-scm.com/downloads](https://git-scm.com/downloads).
2. Under **Downloads**, click **Mac OS X**.
3. When the download completes, double-click the `.dmg` file open the installer package.
4. Double-click the installer package to begin the installation.
    > *Security Warning*
    >
    > You may see a warning message that the package can't be opened because it's not from a recognized developer. 
    If this happens, go to System Preferences > Security and Privacy Settings, and click Open Anyway.
5. Click **Continue** for the installation, and enter your local password to authorize the installation.

##### Windows:

1. Go to [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Under **Downloads**, click on **Windows**.
3. When the dialog opens asking if you want to allow the app to make changes to your device, click Yes.
4. Follow the steps in the setup wizard to complete the installation. You should accept all the default settings.
<br />

### Install Python


##### MacOSX:
1. Using `brew` install `python`:
   
    ```
    $ brew install python3
    ```
    Python 2.7 is included by default on recent versions of Mac OSs. If it somehow not included, install it by running ```brew install python```
    
2. (Optional) Install `pip` to manage packages. Modern versions of Python come with `pip` included. To  verify if you have `pip` installed, run

    ```
    pip -V
    ```

    in your command prompt. You should see something like this:

    ```
    pip 18.1 from /path/of/python/installation
    ```
    
    If you get an error or "pip not found" message, you can install `pip` separately using the following commands:

    ```
    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py
    $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ python get-pip.py
    ```
    
3. Install `virtualenv` in order to manage projects that have different or conflicting dependencies--it also prevents you from accidentally installing global python dependencies.
    ```
    $ pip install virtualenv
    ```

    
##### Windows:
1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Click the "Download Python `<version>`" button.
3. Download the package and extract it on you system.
4. Open the executable and follow the prompts to complete installation.

### Install an IDE

It's recommended to install and Integrated Developer Environment, or a text editor, to help manage package dependencies, interperters, and overall code execution. There are several options available, some of them are free and some require payment:

* [PyCharm](https://www.jetbrains.com/pycharm/download/) community edition is free, Professional version requires subscription.
* [Visual Studio Code](https://code.visualstudio.com/Download) free text editor from Microsoft with a wide variety of extensions.
* [Komodo Edit](https://www.activestate.com/komodo-edit), free, text editor, stripped down version of [Komodo IDE](https://www.activestate.com/products/komodo-ide/features/) (paid version).

### Setup the Project
    
1. Setup `python` interpreter:
    * In your IDE, select an interpreter that references the version of Python installed on your system. Below are links to the relevant documentation for each IDE:
        * [Setup Interpreter in PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
        * [Setup Interpreter in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
        * [Setup Interpreter in Komodo IDE](http://docs.komodoide.com/Manual/tutorial/pythontut#python-tutorial-komodo-ide-only_analyzing-the-python-files_setting-up-the-preprocess-py-program_lines-59-to-65-importing-standard-python-modules)
    
    * (Recommended) Use a `virtualenv` to manage dependencies. See the following documentation for more details:
        * [Setup `virtualenv` in PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
        * [Setup `virtualenv` in Komodo IDE](http://docs.komodoide.com/Manual/tutorial/pythontut#python-tutorial-komodo-ide-only_analyzing-the-python-files_setting-up-the-preprocess-py-program_lines-59-to-65-importing-standard-python-modules)
        * [Configure `virtualenv` in the command line](https://virtualenv.pypa.io/en/latest/userguide/#usage)

2. Install the latest Selenium library for use in the script:

```
pip install selenium
```
    
3. Run the Test Script
    * In order to run the test on [www.saucelabs.com](www.saucelabs.com), change the values of the **`SAUCE_USERNAME`** and **`SAUCE_ACCESS_KEY`** variables in the test script to your Sauce Username and Sauce Access Key values.

    > To retrieve this information, login to your saucelabs.com account and navigate to **User Settings**; there it displays your username and access key.
    
    * Run the following command to test your python script:
        ```
        $ python pytest/instant-sauce-pytest1.py
        ```
        
    * You may also use 'Run Configurations' in your IDE. For directions on how to setup Run/Debug Configurations refer to Documentation:
        * [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html)
        * [Visual Studio Code Documentation](https://code.visualstudio.com/docs/editor/debugging)
        * [Komodo Edit Documentation](http://docs.komodoide.com/manual)