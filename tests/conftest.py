import pytest
from selenium import webdriver


#@pytest.fixture(params=["chrome","firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    #browser = request.param
    print(f"Creating {browser} Driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    elif browser == "safari":
        my_driver = webdriver.Safari()
    else:
        raise TypeError(f"Expected 'chrome','firefox' or 'safari', but got {browser}")
    yield my_driver
    print(f"Closing {browser} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome, firefox "
                                                                         "or safari)")
