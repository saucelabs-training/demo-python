*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library          BindingsLibrary.py


*** Test Cases ***
Valid Login with Standard User
	[Setup]  Start Session  ${BROWSER_NAME}  ${TEST_NAME}
	Open Login Page

	Login As Standard User

	Is On Inventory Page
	[Teardown]  End Session  ${TEST_STATUS}
