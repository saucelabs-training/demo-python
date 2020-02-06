class Reports(object):

    def __init__(self, testobject):
        self.testobject = testobject

    def get_test_report(self, test_report_id):
        method = 'GET'
        endpoint = '/v2/reports/{test_report_id}'.format(test_report_id=test_report_id)

        response = self.testobject.request(method, endpoint)

        return response
    
    def get_screenshot(self, test_report_id, screenshot_id):
        method = 'GET'
        endpoint = '/v2/screenshots/{test_report_id}/{screenshot_id}.png'.format(test_report_id=test_report_id, screenshot_id=screenshot_id)

        response = self.testobject.request(method, endpoint)

        return response

    def get_video(self, video_id):
        method = 'GET'
        endpoint = '/v2/video/{video_id}.mp4'.format(video_id=video_id)

        response = self.testobject.request(method, endpoint)

        return response

    def get_appium_log(self, test_report_id):
        method = 'GET'
        endpoint = '/v2/logs/{test_report_id}/appium'.format(test_report_id=test_report_id)
        
        response = self.testobject.request(method, endpoint)

        return response

    def get_device_log(self, test_report_id):
        method = 'GET'
        endpoint = '/v2/logs/{test_report_id}/device'.format(test_report_id=test_report_id)
        
        response = self.testobject.request(method, endpoint)

        return response

    def get_vitals_log(self, test_report_id):
        method = 'GET'
        endpoint = '/v2/logs/{test_report_id}/vitals'.format(test_report_id=test_report_id)
        
        response = self.testobject.request(method, endpoint)

        return response

    def get_xcuitest_log(self, test_report_id):
        method = 'GET'
        endpoint = '/v2/logs/{test_report_id}/xcuitest'.format(test_report_id=test_report_id)

        response = self.testobject.request(method, endpoint)

        return response