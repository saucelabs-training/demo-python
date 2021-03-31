## Python-Robot-Selenium

This is a sample framework for working with Robotframework and Sauce Labs. It makes use of the pabot plugin for parallelization and selenium2library for working with Selenium and Sauce. This sample does work with Python 2.7 and Python 3.6.

This code is provided on an "AS-IS” basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. Your tests and testing environments may require you to modify this framework. Issues regarding this framework should be submitted through GitHub. For questions regarding Sauce Labs integration, please see the Sauce Labs documentation at https://wiki.saucelabs.com/. This framework is not maintained by Sauce Labs Support.

### Note: Robot framework does not currently support Microsoft Edge. However, if you set the robot browser to firefox and then specify "MicrosoftEdge" in the desired capabilities for Sauce Labs, the tests will run as expected. 

### Environment Setup

1. Global Dependencies
    * [Install Python](https://www.python.org/downloads/)
    * Or Install Python with [Homebrew](http://brew.sh/)
    ```
    $ brew install python
    ```
    * Install [pip](https://pip.pypa.io/en/stable/installing/) to install packages

2. Sauce Credentials
    * In the terminal export your Sauce Labs Credentials as environmental variables:
    ```
    $ export SAUCE_USERNAME=<your Sauce Labs username>
	$ export SAUCE_ACCESS_KEY=<your Sauce Labs access key>
    ```
3. Project Dependencies
	* Install packages (Use sudo if necessary)
	```
	$ pip install -r requirements.txt
	```
### Running Tests

Tests in Series: To run tests in parallel, use the `robot` executor and a browser config file like this:

```
robot -A chrome_config.txt Tests/
```

Tests in Parallel: To run tests in parallel against a single browser, use the `pabot` executor and run one of
```
pabot -A chrome_config.txt Tests/
pabot -A firefox_config.txt Tests/
pabot -A ie_config.txt Tests/
```
and to run all tests in parallel across all browsers, run
```
pabot --argumentfile1 chrome_config.txt --argumentfile2 firefox_config.txt --argumentfile3 ie_config.txt Tests/
```

[Sauce Labs Dashboard](https://app.saucelabs.com/dashboard)

### Advice/Troubleshooting

1. There may be additional latency when using a remote webdriver to run tests on Sauce Labs. Timeouts or Waits may need to be increased.
    * [Selenium tips regarding explicit waits](https://wiki.saucelabs.com/display/DOCS/Best+Practice%3A+Use+Explicit+Waits)

### Resources
##### [Sauce Labs Documentation](https://wiki.saucelabs.com/)

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)

##### [Python 2 Documentation](https://docs.python.org/2.7/)

##### [Python 3 Documentation](https://docs.python.org/3.6/)

##### [Robot Framework Documentation](http://robotframework.org/#documentation)

##### [Page Objects with RobotFramework Example](https://github.com/markwinspear/RobotFramework-layered-sauce-start)

##### [Pabot Plugin Documentation](https://github.com/mkorpela/pabot/blob/master/README.md)

##### [Stack Overflow](http://stackoverflow.com/)
* A great resource to search for issues not explicitly covered by documentation.
