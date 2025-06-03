*** Settings ***
Library  SeleniumLibrary

*** Variables ***

${browser}          ${browserName}
${remote_url}       ${DATA_CENTER}

&{Sauce capabilities}  build=Python-Robot-Selenium-VDC  name=${SUITE_NAME}  username=%{SAUCE_USERNAME}  accessKey=%{SAUCE_ACCESS_KEY}

*** Keywords ***

Open login page
    Open browser  https://www.saucedemo.com/v1/  browser=${browser}
    ...  remote_url=${remote_url}
    ...  options=set_capability("sauce:options", ${Sauce capabilities}); platform_name="${platform}"; browser_version="${version}"

Open inventory page
    Open browser  https://www.saucedemo.com/v1/inventory.html  browser=${browser}
    ...  remote_url=${remote_url}
    ...  options=set_capability("sauce:options", ${Sauce capabilities}); platform_name="${platform}"; browser_version="${version}"

Login As Standard User

    Input text  id:user-name  standard_user
	Input text  id:password  secret_sauce
	Click button  class:btn_action


Login As Invalid User

    Input text  id:user-name  invalid
	Input text  id:password  invalid
	Click button  class:btn_action

Add Item To Cart

    Click button  class:btn_primary


Remove Item From Cart

	Click button  class:btn_secondary


Has Items In Cart

	Page should contain element  class:shopping_cart_badge

End Session
    Run Keyword If  '${TEST_STATUS}'== 'PASS'  Execute Javascript  sauce:job-result=passed
    ...  ELSE  Execute Javascript  sauce:job-result=failed
    Close Browser
