from saucebindings.session import SauceSession


class TestAccessibilitySauce(object):

    def test_creates_session(self):
        session = SauceSession()
        driver = session.start()

        driver.get('https://www.saucedemo.com/')

        session.accessibility_results()
        session.stop(True)
