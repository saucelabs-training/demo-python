*** Settings ***
Documentation     A test suite with a single test for invalid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot


*** Test Cases ***
Invalid Login with Invalid User
	Start Session

	Login As Invalid User

	Page should contain element  accessibility_id=test-Error message
	[Teardown]  End Session

