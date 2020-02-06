import logging
import logging.config
import requests

from testobject.devices import Devices
from testobject.suites import Suites
from testobject.watcher import Watcher
from testobject.storage import Storage
from testobject.reports import Reports

logger = logging.getLogger(__name__)


class NoPasswordException(Exception):
    pass


class TestObject(object):

    URL_BASE = "https://app.testobject.com/api/rest"

    def __init__(self, username, api_key, password=None):

        self.username = username
        self.api_key = api_key
        self.password = password
        self.devices = Devices(self)
        self.suites = Suites(self)
        self.watcher = Watcher(self)
        self.storage = Storage(self)
        self.reports = Reports(self)

    def request(self, method, endpoint, auth_type=None, data=None, binary_file=None, **kwargs):
        url = TestObject.URL_BASE + endpoint
        logger.info("URL: %s", url)

        auth = None

        # Appium Suites API needs a different authentication
        # "All endpoints in Appium Suites API require basic authentication with
        # the API Key as the username and the password left blank."
        # Watcher API needs no authentication
        if auth_type == 'suite':
            auth = (self.api_key, '')
        elif auth_type == 'watcher':
            pass
        elif auth_type == 'session_reports':
            if self.password:
                auth = (self.username, self.password)
            else:
                raise NoPasswordException
        else:
            auth = (self.username, self.api_key)

        content = requests.request(method, url, auth=auth, json=data, data=binary_file, **kwargs)

        logger.debug("content: %s", content)

        return content
