import time
from selenium.webdriver.support.ui import Select

class Addcustomer:
    #Add cutomer page
    lnkcustomers_menu_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    lnkcustomers_menuitem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btnAddnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath ="//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "//input[@id='Gender_Male']"
    rdFemaleGender_id = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath= "//label[@id='SelectedCustomerRoleIds_label']"
    lstitemAdministrators_xpath = "//span[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//span[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//span[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//span[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkcustomers_menu_xpath).click()

    def clickOnCustomersMenuitem(self):
        self.driver.find_element_by_xpath(self.lnkcustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered (or) Guest,only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()