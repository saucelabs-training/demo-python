*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot


*** Test Cases ***
Valid Login with Standard User
	Start Session

	Login As Standard User

	Page should contain element  accessibility_id=test-PRODUCTS
	[Teardown]  End Session
