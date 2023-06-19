from saucebindings.session import SauceSession
from saucebindings.session import SauceOptions

def test_from_gitpod(driver):
    options = SauceOptions('firefox')
    options.browser_version = '106'
    options.platform_name = 'Windows 11'
    options.build = '<your build id>'
    options.name = '<your test name>'
    sauce = SauceSession(options=options)
    sauce.start()
    title = sauce.title
    assert "" in title
    
