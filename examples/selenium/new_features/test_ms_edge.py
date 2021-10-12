from selenium.webdriver.edge.options import Options as EdgeOptions


# Selenium 3 only supported EdgeHTML without any custom methods
# Selenium 4 supports same capabilities as Chrome

def test_edge_options():
    options = EdgeOptions()
    options.add_argument('foo')
    options.binary_location = '/path/to/edge'
    options.add_encoded_extension('encoded')

    caps = options.to_capabilities()

    edgeOptions = caps['ms:edgeOptions']
    assert edgeOptions['args'] == ['foo']
    assert edgeOptions['binary'] == '/path/to/edge'
    assert edgeOptions['extensions'] == ['encoded']
