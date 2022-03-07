import random
import string

import pytest
from selenium.common.exceptions import InvalidSelectorException
from PageObjects.Addcustomerpage import Addcustomer
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readproperties import ReadConfig

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*****Test_003_AddCustomer******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login successful******")

        self.logger.info("*****Starting Add Customer Test ******")
        self.addcust= Addcustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuitem()

        self.addcust.clickOnAddnew()

        self.logger.info("*****Providing Customer info ******")

        self.email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        #self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Shirey")
        self.addcust.setLastName("Rasper")
        self.addcust.setDob("07/05/1989")
        self.addcust.setCompanyName("TechJobs")
        self.addcust.setAdminContent("This is for testing......")
        #self.addcust.setGender("Male")
        self.addcust.clickOnSave()

        self.logger.info("*****Saving Customer info ******")

        self.logger.info("*****Add Customer validation started ******")
        self.msg=self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("*****Add Customer Test Passed******")
        else:
             self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png") #Screenshot
             self.logger.error("********Add customer Test Failed******")
             assert True==False

        self.driver.close()
        self.logger.info("***** Ending Home Page Title Test*********")

def random_generator(size=8,chars=string.ascii_lowercase + string.digits) :
    return ''.join(random.choice(chars) for x in range(size))













