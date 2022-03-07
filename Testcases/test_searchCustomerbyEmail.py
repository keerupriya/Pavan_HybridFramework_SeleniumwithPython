import time
import pytest

from PageObjects.Addcustomerpage import Addcustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_004_SearchCustomerByEmail :
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerbyEmail(self,setup):
        self.logger.info("*****SearchCustomerByEmail_004******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login successful******")

        self.logger.info("*****Starting Search Customer By Email ******")

        self.addcust= Addcustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuitem()

        self.logger.info("*****Searching Customer by EmailID ******")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("********TC_Test_004_:SearchCustomerByEmail Finished")
        self.driver.close();










