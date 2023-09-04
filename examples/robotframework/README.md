# Using Robot Framework with Sauce Labs

If you are reading this, you are likely interested in running tests on Sauce Labs devices with Robot Framework tests in Python. If you using Robot Framework with Java, you will need help from elsewhere. 

## Basic Installation

All of these examples assumes you are using Robot Framework version 4.0+. Following the [main README](../../README.md) installation instructions will install Robot Framework and needed libraries.

## Running Tests

To illustrate running tests in parallel, these examples use [pabot](https://pabot.org/) as the test runner. You can replace `pabot` with `robot` in all of the following to run tests in series.

### Standard Execution Using pabot

To execute desktop web tests in parallel using Selenium, run

```bash
pabot --argumentfile1 examples/robotframework/desktop_web/chrome_config.txt --argumentfile2 examples/robotframework/desktop_web/firefox_config.txt --argumentfile3 examples/robotframework/desktop_web/ie_config.txt --variable DATA_CENTER:'https://ondemand.eu-central-1.saucelabs.com/wd/hub' examples/robotframework/desktop_web/Tests/
```

To execute native mobile tests in parallel using Appium with an Android app, run
```bash
pabot --variable DATA_CENTER:'https://ondemand.eu-central-1.saucelabs.com/wd/hub' -A examples/robotframework/native_mobile/android/android_config.txt examples/robotframework/native_mobile/android/tests/"
```

To execute native mobile tests in parallel using Appium with an iOS app, run
```bash
pabot --variable DATA_CENTER:'https://ondemand.eu-central-1.saucelabs.com/wd/hub' -A examples/robotframework/native_mobile/android/android_config.txt examples/robotframework/native_mobile/ios/tests/"
```

Note you do need to set the variable for `DATA_CENTER` wth the full Data Center URL currently. The above examples uses the EU data center as Robot Framework is often more comment with EU teams.

### Running with Poetry

To execute desktop web tests in parallel using Selenium, run

```bash
poetry run pabot --argumentfile1 examples/robotframework/desktop_web/chrome_config.txt --argumentfile2 examples/robotframework/desktop_web/firefox_config.txt --argumentfile3 examples/robotframework/desktop_web/ie_config.txt --variable DATA_CENTER:'https://ondemand.eu-central-1.saucelabs.com/wd/hub' examples/robotframework/desktop_web/Tests/
```

To execute native mobile tests in parallel using Appium with an Android app, run

```bash
poetry run pabot --variable DATA_CENTER:'https://ondemand.eu-central-1.saucelabs.com/wd/hub' -A examples/robotframework/native_mobile/android/android_config.txt examples/robotframework/native_mobile/android/tests/"
```

To execute native mobile tests in parallel using Appium with an iOS app, run

```bash
poetry run pabot --variable DATA_CENTER:'https://ondemand.eu-central-1.saucelabs.com/wd/hub' -A examples/robotframework/native_mobile/android/android_config.txt examples/robotframework/native_mobile/ios/tests/"
```

Note you do need to set the variable for `DATA_CENTER` wth the full Data Center URL currently. The above examples uses the EU data center as Robot Framework is often more comment with EU teams.

### Running with Pipenv

To execute desktop web tests in parallel using Selenium, run

```bash
pipenv run robot-desktop-web-eu
```

To execute native mobile tests in parallel using Appium with an Android app, run

```bash
pipenv run robot-android-eu
```

To execute native mobile tests in parallel using Appium with an iOS app, run

```bash
pipenv run robot-ios-eu
```

Obviously, you can change the `eu` to `us` in the above pipenv examples to execute on US data center devices.






