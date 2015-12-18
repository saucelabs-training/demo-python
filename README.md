# Python-Pytest-Appium-Android

```
$ export SAUCE_USERNAME=your_username
$ export SAUCE_ACCESS_KEY=your_access_key
```

# Setup
* The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
```$ pip install virtualenv```
* Create a virtual environment in your project folder the environment name is arbitrary.
```$ virtualenv venv```
* Activate the environment:
```$ source venv/bin/activate```
* Install the required packages:
```$ pip install -r requirements.txt```

# Running tests: -n option designates number of parallel tests and -s to disable output capture.
```$ py.test -s -n 10 tests```

# Kown Issues:
* Test output will be captured in .testlog files as the pytest-xdist plugin has issues with not capturing stdout and stderr. You can use the following commands to output session id's for CI integration and clean up.
```
$ cat *.testlog
$ rm -rf *.testlog
```
