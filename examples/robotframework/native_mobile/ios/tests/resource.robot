*** Settings ***
Library  AppiumLibrary

*** Variables ***
${PLATFORM_NAME}        %{platformName}
${DEVICE_NAME}          %{deviceName}
${PRIVATE_DEVICES_ONLY}  %{privateDevicesOnly}
${REMOTE_URL}       ${DATA_CENTER}

*** Keywords ***
Start Session
    Open application  ${REMOTE_URL}
    ...  platformName=${PLATFORM_NAME}
    ...  deviceName=${DEVICE_NAME}
    ...  username=%{SAUCE_USERNAME}
    ...  accessKey=%{SAUCE_ACCESS_KEY}
    ...  privateDevicesOnly=${PRIVATE_DEVICES_ONLY}
    ...  app=storage:filename=iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.7.0.ipa
    ...  name=${TEST_NAME} 

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
