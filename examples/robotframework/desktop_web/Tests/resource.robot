*** Settings ***
Library  SeleniumLibrary
Library  w3c_options.py

*** Variables ***

${browser}          ${browserName}  # could set this to Chrome
${remote_url}       ${DATA_CENTER}  # could set this to https://ondemand.eu-central-1.saucelabs.com/wd/hub

*** Keywords ***

Open login page
    ${capabilities}=  w3c_options.Browsers  Chrome  latest  Windows 10
    Open browser  https://www.saucedemo.com/v1/  browser=${browser}
    ...  remote_url=${remote_url}
    ...  desired_capabilities=${capabilities}

Open inventory page
    ${capabilities}=  w3c_options.Browsers   ${latest}  ${Chrome}  ${Windows 10} 
    Open browser  https://www.saucedemo.com/v1/inventory.html  browser=${browserName}
    ...  remote_url=${remote_url}
    ...  desired_capabilities=${capabilities}

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
