from tkinter.tix import Select

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By


class RegisterPage:
    name_name = "name"
    email_name = "email"
    password_id = "exampleInputPassword1"
    checkBox_id = "exampleCheck1"
    genderDropDown_id = "exampleFormControlSelect1"
    empStaRadioBtn_id = "inlineRadio1"
    dob_name = "bday"
    submitBtn_className = "btn.btn-success"
    
    def __init__(self,driver):
        self.driver = driver

    def setName(self,name):
        self.driver.find_element(By.NAME,self.name_name).clear()
        self.driver.find_element(By.NAME,self.name_name).send_keys(name)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.email_name).clear()
        self.driver.find_element(By.NAME,self.email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def setCheckBox(self):
        self.driver.find_element(By.ID,self.checkBox_id).click()

    def setGenderDropDown(self):
        dropDown = Select(self.driver.find_element(By.ID, self.genderDropDown_id))
        allOption = dropDown.options
        for i in allOption:
            if i.text == "Male":
                i.click()

    def setEmpStaRadioBtn(self):
        self.driver.find_element(By.ID,self.empStaRadioBtn_id).click()

    def setDob(self,dob):
        self.driver.find_element(By.NAME,self.dob_name).clear()
        self.driver.find_element(By.NAME,self.dob_name).send_keys(dob)

    def setSubmitBtn(self):
        self.driver.find_element(By.CLASS_NAME,self.submitBtn_className).click()
