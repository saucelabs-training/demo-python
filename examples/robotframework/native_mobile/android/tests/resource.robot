*** Settings ***
Library  AppiumLibrary

*** Variables ***
${PLATFORM_NAME}        %{platformName} 
${PLATFORM_VERSION}     %{platformVersion}
${DEVICE_ORIENTATION}   %{deviceOrientation}
${PRIVATE_DEVICES_ONLY}  %{privateDevicesOnly}
${REMOTE_URL}       ${DATA_CENTER}

*** Keywords ***
Start Session
    Open application  ${REMOTE_URL}
    ...  platformName=${PLATFORM_NAME}
    ...  platformVersion=${PLATFORM_VERSION}
    ...  deviceOrientation=${DEVICE_ORIENTATION}
    ...  username=%{SAUCE_USERNAME}
    ...  accessKey=%{SAUCE_ACCESS_KEY}
    ...  privateDevicesOnly=${PRIVATE_DEVICES_ONLY}
    ...  app=https://github.com/saucelabs/sample-app-mobile/releases/download/2.7.1/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk
    ...  name=${TEST_NAME}  

End Session
    Run Keyword If  '${TEST_STATUS}'== 'PASS'  Execute Script  sauce:job-result=passed
    ...  ELSE  Execute Script  sauce:job-result=failed
    Close all applications

Login As Standard User

    Input text  accessibility_id=test-Username  standard_user
	Input text  accessibility_id=test-Password  secret_sauce
	Click element  accessibility_id=test-LOGIN

Login As Invalid User

    Input text  accessibility_id=test-Username  invalid
	Input text  accessibility_id=test-Password  invalid
	Click element  accessibility_id=test-LOGIN 