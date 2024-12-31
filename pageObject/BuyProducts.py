from selenium.webdriver.common.by import By

class BuyProducts:
    clickShop = "Shop"
    item1 = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[1]/div/div[2]/button"
    item2 = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[2]/div/div[2]/button"
    item3 = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[3]/div/div[2]/button"
    item4 = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[4]/div/div[2]/button"
    checkOut1 = "nav-link.btn.btn-primary"
    removeBlkBrr = "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[4]/td[5]/button"
    checkOut2 = "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[5]/td[5]/button"
    countryXP = "//*[@id='country']"
    checkboxXP = "/html/body/app-root/app-shop/div/app-checkout/div[1]/div[2]"
    purchase_className = "btn.btn-success.btn-lg"

    def __init__(self,driver):
        self.driver = driver


    def setClickShop(self):
        self.driver.find_element(By.LINK_TEXT,self.clickShop).click()

    def setItem1(self):
        self.driver.find_element(By.XPATH, self.item1).click()

    def setItem2(self):
        self.driver.find_element(By.XPATH, self.item2).click()

    def setItem3(self):
        self.driver.find_element(By.XPATH, self.item3).click()

    def setItem4(self):
        self.driver.find_element(By.XPATH, self.item4).click()

    def setCheckOut1(self):
        self.driver.find_element(By.CLASS_NAME, self.checkOut1).click()

    def setRemoveBlkBrr(self):
        self.driver.find_element(By.XPATH, self.removeBlkBrr).click()

    def setCheckOut2(self):
        self.driver.find_element(By.XPATH, self.checkOut2).click()

    def setCountry(self,country):
        self.driver.find_element(By.XPATH, self.countryXP).clear()
        self.driver.find_element(By.XPATH, self.countryXP).send_keys = country

    def setCheckBox(self):
        self.driver.find_element(By.XPATH, self.checkboxXP).click()

    def setPurchase_className(self):
        self.driver.find_element(By.CLASS_NAME, self.purchase_className).click()