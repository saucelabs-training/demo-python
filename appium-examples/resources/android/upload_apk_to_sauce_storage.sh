this_path=$(pwd)

curl -u $SAUCE_USERNAME:$SAUCE_ACCESS_KEY -X POST -H "Content-Type: application/octet-stream" https://saucelabs.com/rest/v1/storage/$SAUCE_USERNAME/SwagLabsMobileApp.apk?overwrite=true --data-binary @$this_path/Android.SauceLabs.Mobile.Sample.app.2.2.1.apk
