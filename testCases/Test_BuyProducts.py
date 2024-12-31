from Project_2.pageObject.BuyProducts import BuyProducts


class Test_BuyProducts:
    country = "India"
    buyProdURL = "https://rahulshettyacademy.com/angularpractice/shop"

    def test_checkURL(self, setUp):
        self.driver = setUp
        self.driver.get(self.buyProdURL)
        actTitle = self.driver.title
        expTitle = "ProtoCommerce"
        if actTitle == expTitle:
            assert True
        else:
            assert False

    def test_buyProducts(self,setUp):
        self.driver = setUp
        self.driver.get(self.buyProdURL)
        self.obj_buyProd = BuyProducts(self.driver)
        self.obj_buyProd.setClickShop()
        self.obj_buyProd.setItem1()
        self.obj_buyProd.setItem2()
        self.obj_buyProd.setItem3()
        self.obj_buyProd.setItem4()
        self.obj_buyProd.setCheckOut1()
        self.obj_buyProd.setRemoveBlkBrr()
        self.obj_buyProd.setCheckOut2()
        self.obj_buyProd.setCountry(self.country)
        self.obj_buyProd.setCheckBox()
        self.obj_buyProd.setPurchase_className()