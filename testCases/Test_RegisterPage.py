import time
from pageObject.RegisterPage import RegisterPage


class Test_RegisterPage:
    registerPageURL = "https://rahulshettyacademy.com/angularpractice/"
    name = "Rahul"
    email = "rahul@test.com"
    password = "123456"
    dob = 12/30/2024

    def test_checkURL(self,setUp):
        self.driver = setUp
        self.driver.get(self.registerPageURL)
        actTitle = self.driver.title
        exp_title = "ProtoCommerce"
        if actTitle ==  exp_title:
            assert True
        else:
            assert False

    def test_registerLogin(self,setUp):
        self.driver = setUp
        self.driver.get(self.registerPageURL)
        self.obj_registerPage = RegisterPage(self.driver)
        self.obj_registerPage.setName(self.name)
        self.obj_registerPage.setEmail(self.email)
        self.obj_registerPage.setPassword(self.password)
        self.obj_registerPage.setCheckBox()
        self.obj_registerPage.setGenderDropDown()
        self.obj_registerPage.setEmpStaRadioBtn()
        self.obj_registerPage.setDob(self.dob)
        self.obj_registerPage.setSubmitBtn()
        
        time.sleep(3)
