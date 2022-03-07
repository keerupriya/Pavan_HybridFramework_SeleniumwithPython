from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


#############       Pytest HTML Report       ############

def pytest_configure(config):
    config._metadata['project Name'] = 'Pavan_HybridFramework'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'


# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
#To Run tests on desired browser
#pytest -v -s Testcases/test_login.py --browser chrome
#pytest -v -s Testcases/test_login.py --browser firefox

#To run tests parallel
#pytest -v -s -n=2 Testcases/test_login.py --browser chrome
#pytest -v -s -n=2 Testcases/test_login.py --browser firefox

#generate pytest HTML reports
##pytest -v -s -n=2 --html=Reports\report.html Testcases/test_login.py --browser chrome

 #pytest -v -s --html=Reports\report.html Testcases/test_login_ddt.py --browser chrome
