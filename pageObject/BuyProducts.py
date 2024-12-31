from selenium.webdriver.common.by import By

class BuyProducts:
    clickShop_linkText = "Shop"
    item1_xpath = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[1]/div/div[2]/button"
    item2_xpath = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[2]/div/div[2]/button"
    item3_xpath = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[3]/div/div[2]/button"
    item4_xpath = "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[4]/div/div[2]/button"
    checkOut1_className = "nav-link.btn.btn-primary"
    removeBlkBrr_xpath = "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[4]/td[5]/button"
    checkOut2_xpath = "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[5]/td[5]/button"
    country_xpath = "//*[@id='country']"
    checkbox_xpath = "/html/body/app-root/app-shop/div/app-checkout/div[1]/div[2]"
    purchase_className = "btn.btn-success.btn-lg"

    def __init__(self,driver):
        self.driver = driver


    def setClickShop(self):
        self.driver.find_element(By.LINK_TEXT,self.clickShop_linkText).click()

    def setItem1(self):
        self.driver.find_element(By.XPATH, self.item1_xpath).click()

    def setItem2(self):
        self.driver.find_element(By.XPATH, self.item2_xpath).click()

    def setItem3(self):
        self.driver.find_element(By.XPATH, self.item3_xpath).click()

    def setItem4(self):
        self.driver.find_element(By.XPATH, self.item4_xpath).click()

    def setCheckOut1(self):
        self.driver.find_element(By.CLASS_NAME, self.checkOut1_className).click()

    def setRemoveBlkBrr(self):
        self.driver.find_element(By.XPATH, self.removeBlkBrr_xpath).click()

    def setCheckOut2(self):
        self.driver.find_element(By.XPATH, self.checkOut2_xpath).click()

    def setCountry(self,country):
        self.driver.find_element(By.XPATH, self.country_xpath).clear()
        self.driver.find_element(By.XPATH, self.country_xpath).send_keys = country

    def setCheckBox(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()

    def setPurchase_className(self):
        self.driver.find_element(By.CLASS_NAME, self.purchase_className).click()
