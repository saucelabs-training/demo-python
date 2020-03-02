*** Settings ***
Library  AppiumLibrary

*** Variables ***
${KEY}                  %{TESTOBJECT_SAMPLE_IOS}
${PLATFORM_NAME}        %{platformName} 
${PLATFORM_VERSION}     %{platformVersion}
${DEVICE_ORIENTATION}   %{deviceOrientation}
${PRIVATE_DEVICES_ONLY}  %{privateDevicesOnly}
${REMOTE_URL}       http://us1.appium.testobject.com/wd/hub/

*** Keywords ***
Start Session
    Open application  ${REMOTE_URL}  platformName=${PLATFORM_NAME}  platformVersion=${PLATFORM_VERSION}  deviceOrientation=${DEVICE_ORIENTATION}  browserName=''  testobject_api_key=${KEY}  privateDevicesOnly=${PRIVATE_DEVICES_ONLY}  name=${TEST_NAME}  

End Session
    Close all applications

Login As Standard User

    Input text  accessibility_id=test-Username  standard_user
	Input text  accessibility_id=test-Password  secret_sauce
	Click element  accessibility_id=test-LOGIN

Login As Invalid User

    Input text  accessibility_id=test-Username  invalid
	Input text  accessibility_id=test-Password  invalid
	Click element  accessibility_id=test-LOGIN
