import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/Logindata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*****Test_002_DDT_Login******")
        self.logger.info("*****Verifying Login DDT test******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows=ExcelUtils.getRowCount(self.path,'Sheet1')
        print(" Number of Rows i a Excel:",self.rows)

        lst_status=[]    #Empty list variable

        for r in range(2,self.rows+1):
           self.user= ExcelUtils.readData(self.path,'Sheet1',r,1)
           self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
           self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

        self.lp.setUserName(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)

        act_title = self.driver.title
        exp_title= "Dashboard / nopCommerce administration"

        if act_title == exp_title:
            if self.exp=="Pass":
                self.logger.info("***Passed******")
                self.lp.clickLogout();
                lst_status.append("Pass")
            elif self.exp=="Fail":
                self.logger.info("***failed*******")
                self.lp.clickLogout();
                lst_status.append("Fail")
        elif act_title != exp_title:
              if self.exp=="Pass":
                self.logger.info("***failed******")
                lst_status.append("Fail")
              elif self.exp=='Fail':
                self.logger.info("***passed*****")
                lst_status.append("Pass")

        if "Fail" not in lst_status:
          self.logger.info("***** Login DDT test passed****")
          self.driver.close()
          assert True
        else:
         self.logger.info("*****Login DDT test failed****")
         self.driver.close()
         assert False

         self.logger.info("*****End of Login DDT test ****")
         self.logger.info("***** completed TC_LoginDDT_002****");



