*** Settings ***
Documentation     A test suite with a single test for invalid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot


*** Test Cases ***

Invalid Login with Invalid User
	Open Login Page

	Login As Invalid User

	Page should contain element  class:error-button
	[Teardown]  End Session

