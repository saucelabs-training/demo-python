class Watcher(object):

    def __init__(self, testobject):
        self.testobject = testobject

    def skip_test_report(self, session_id):
        method = 'PUT'
        endpoint = '/v2/appium/session/{session_id}/skiptest'.format(session_id=session_id)

        content = self.testobject.request(method, endpoint, auth_type='watcher')

        return content

    def report_test_result(self, session_id, passed):
        method = 'PUT'

        endpoint = '/v2/appium/session/{session_id}/test'.format(session_id=session_id)

        data = {}
        data['passed'] = passed

        content = self.testobject.request(method, endpoint, auth_type='watcher', data=data)

        return content
