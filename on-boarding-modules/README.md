# Sauce Labs On-Boarding Python Examples

The following scripts provide quick examples to test your connection to Sauce Labs. Each script, titled `module<#>-<framework_name>`, represents a module from the "Getting Started" tab in the Sauce labs UI.

### Module List

- [Sauce Labs On-Boarding Python Examples](#sauce-labs-on-boarding-python-examples)
    - [Module List](#module-list)
    - [Module 1: Running your first test](#module-1-running-your-first-test)
    - [Module 2: Testing against your own application](#module-2-testing-against-your-own-application)
    - [Module 3: Adding `sauce:options` and `chrome options`](#module-3-adding-sauceoptions-and-chrome-options)
    - [Module 4: Adjusting timeouts, delays, and build tags](#module-4-adjusting-timeouts-delays-and-build-tags)

<br />

> All examples below use the pytest framework

### Module 1: Running your first test

Open the script `test_module1_pytest.py`, and ensure you've exported (or hardcoded, but not recommended) your [Sauce Labs Account Credentials](https://wiki.saucelabs.com/display/DOCS/Best+Practice%3A+Use+Environment+Variables+for+Authentication+Credentials) in the following lines:

```
sauce_username = os.environ["SAUCE_USERNAME"]
sauce_access_key =os.environ["SAUCE_ACCESS_KEY"]
```

Since these onboarding modules are meant to be self-contained set of learning modules, make sure you are in a terminal and in this directory. If you are using MacOS or a Unix/Linux system, run the command

```
pwd
```

and the output should look like

```
/.../demo-python/on-boarding-modules
```

If you are using Windows, run the command
```
cd
```

and the output should look like
```
C:\...\demo-python\on-boarding-modules
```

Install all needed dependencies to execute these modules by running the following:

```
pip install -r requirements.txt
```

Run the following command to run the test:

```
pytest on-boarding-modules/pytest-examples/test_module1_pytest.py
```

<br />

### Module 2: Testing against your own application

Open the script `test_module2_pytest.py`. Edit the following line with your own application URL:

```
driver.get("https://www.saucedemo.com")
```

and also edit the following line with your web application's page title that appears in the browser tab.

```
expected_title = "Swag Labs"
```
Please take notice that if your application is not publicly available the test will fail to make a connection with Sauce Labs. Please read the following wiki page on how to [Setup Sauce Connect Proxy](https://wiki.saucelabs.com/display/DOCS/Sauce+Connect+Proxy) to ensure you're tests can run on Sauce Labs.

<br />

### Module 3: Adding `sauce:options` and `chrome options`

Open the script `test_module3_pytest.py`. Please notice how the script contains a `sauce:options` and `chrome options` declaration.

`sauce:options`:
```
sauceOptions = {
        'screenResolution': '1280x768',
        'seleniumVersion': '3.141.59',
        'build': 'Onboarding Sample App - Python + Pytest',
        'name': '3-cross-browser',
        'username': sauce_username,
        'accessKey': sauce_access_key
    }
```

`chromeOpts`
```
chromeOpts = {
        'platformName': 'Windows 10',
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'goog:chromeOptions': {'w3c': True},
        'sauce:options': sauceOptions
    }
```

This is a Sauce Labs best practice where `sauce:options` handles all [saucelabs.com](www.saucelabs.com)-specific capabilities such as:
`username`, `accesskey`, `build number`, test name, timeouts etc, and in `chromeOpts`, we define browser and/or WebDriver capabilities such as
the `browserName`, `browserVersion`, and `platformName`.

<br />

### Module 4: Adjusting timeouts, delays, and build tags

Open the script `test_module4_pytest.py`. Please notice that the following lines contain some specific `driver` capabilities:

```
'tags': ['instant-sauce', 'pytest', 'module4'],
'maxDuration': 1800,
'commandTimeout': 300,
'idleTimeout': 1000,
```

These test configuration options, allow you to control how long a session will wait for a new test command (`idleTimeout`), the maximum duration for the Sauce Labs VM lifecycle  (`maxDuration`), and the ability to filter test results by specific keywords (`tags`). 

Please read the following wiki page to learn more about [setting build tags](https://wiki.saucelabs.com/display/DOCSDEV/Best+Practice%3A+Use+Build+IDs%2C+Tags%2C+and+Names+to+Identify+Your+Tests) and [controlling build timeouts](https://wiki.saucelabs.com/display/DOCS/Test+Configuration+Options#TestConfigurationOptions-MaximumTestDuration).

Visit the [saucelabs.com automated build page](https://app.saucelabs.com/dashboard/builds) and select the build `Onboarding Sample App - Python` to see the following test case:
    
    ![1-first-test](1-first-test.png)