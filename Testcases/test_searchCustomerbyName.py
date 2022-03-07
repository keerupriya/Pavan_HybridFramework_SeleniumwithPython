import time
import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.Addcustomerpage import Addcustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.customLogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_005_SearchCustomerByName:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerbyName(self,setup):
        self.logger.info("*****SearchCustomerByName_005******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login successful******")

        self.logger.info("*****Starting Search Customer By Name ******")

        self.addcust= Addcustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuitem()

        self.logger.info("*****Searching Customer by Name ******")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Brenda")
        searchcust.setLastName("Lindgren")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Brenda Lindgren")
        assert True==status
        self.logger.info("********TC_Test_004_:SearchCustomerByName Finished")
        self.driver.close();







