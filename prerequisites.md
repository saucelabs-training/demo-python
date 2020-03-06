# Python Prerequisites

* Install [Git](#install-git)
* Install [Python and Pip](#install-python-and-pip)
* Install [a Framework](#install-a-test-framework)
    * [Pytest](#install-pytest)
    * [UnitTest](#install-unittest)
* (Optional) Install an [IDE](#install-an-ide)
    
<br />

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

### Install Python and PIP


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

<br />

### Install a Test Framework
A testing framework is a set of guidelines/rules for desiging test cases. 
Frameworks themselves consist of test and reporting classes that allow QA engineers to test efficiently. 
This repo only supports `pytest` and `unittest`. 

For more information regarding other libraries, checkout our GitHub repo that catalogs all [sample test frameworks](https://github.com/saucelabs-sample-test-frameworks).

<br />

##### Install Pytest
1. Open a terminal (OSX) or command prompt (Windows)
2. Navigate to the pytest directory:
    ```
    cd on-boarding-modules/pytest-examples/
    ```
3. Resolve the package dependencies:
    ```
    sudo pip install -r requirements.txt 
    ```
4. Run tests:
    ```
    pytest
    ```

<br />

##### Install UnitTest
`unittest` is an included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit series of tools.
1. Open a terminal (OSX) or command prompt (Windows)
2. Navigate to the unittest-examples directory:
    ```
    cd on-boarding-modules/unittest-examples
    ```
3. Resolve the package dependencies:
    ```
    sudo pip install -r requirements.txt 
    ```
4. Run tests:
    ```
    python -m unittest
    ```

<br />

### Install an IDE

It's recommended to install and Integrated Developer Environment, or a text editor, to help manage package dependencies, interperters, and overall code execution. There are several options available, some of them are free and some require payment:

* [PyCharm](https://www.jetbrains.com/pycharm/download/) community edition is free, Professional version requires subscription.
* [Visual Studio Code](https://code.visualstudio.com/Download) free text editor from Microsoft with a wide variety of extensions.
* [Komodo Edit](https://www.activestate.com/komodo-edit), free, text editor, stripped down version of [Komodo IDE](https://www.activestate.com/products/komodo-ide/features/) (paid version).

#### Setup a `python` interpreter:
* In your IDE, select an interpreter that references the version of Python installed on your system. Below are links to the relevant documentation for each IDE:
    * [Setup Interpreter in PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
    * [Setup Interpreter in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
    * [Setup Interpreter in Komodo IDE](http://docs.komodoide.com/Manual/tutorial/pythontut#python-tutorial-komodo-ide-only_analyzing-the-python-files_setting-up-the-preprocess-py-program_lines-59-to-65-importing-standard-python-modules)
    
* (Recommended) Use a `virtualenv` to manage dependencies. See the following documentation for more details:
    * [Setup `virtualenv` in PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
    * [Setup `virtualenv` in Komodo IDE](http://docs.komodoide.com/Manual/tutorial/pythontut#python-tutorial-komodo-ide-only_analyzing-the-python-files_setting-up-the-preprocess-py-program_lines-59-to-65-importing-standard-python-modules)
    * [Configure `virtualenv` in the command line](https://virtualenv.pypa.io/en/latest/user_guide.html)
<br />
