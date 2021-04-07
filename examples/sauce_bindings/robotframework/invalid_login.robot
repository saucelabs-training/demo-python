*** Settings ***
Documentation     A test suite with a single test for invalid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library          BindingsLibrary.py


*** Test Cases ***
Invalid Login with Invalid User
	[Setup]  Start Session  ${BROWSER_NAME}  ${TEST_NAME}
	Open Login Page

	Login As Invalid User

	Is Login Error Displayed
	[Teardown]  End Session  ${TEST_STATUS}

