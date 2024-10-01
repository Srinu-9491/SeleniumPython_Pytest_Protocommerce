from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopPageUrl()
        products = checkOutPage.getProducts()
        log.info("All products collected")
        for product in products:
            productNamefromPage = product.find_element(By.XPATH, "div/h4/a").text
            if productNamefromPage == checkOutPage.product_name:
                log.info("Itentified the particular product")
                log.info("Add product to cart")
                product.find_element(By.TAG_NAME, "button").click()

        log.info("Click on Checkout button")
        checkOutPage.getCheckOutButton().click()
        productInCart = checkOutPage.getProductAddedInCart().text
        assert productInCart == checkOutPage.product_name
        log.info("Selected product is added to cart")
        confirmPage = checkOutPage.getCartPageCheckoutButton()
        log.info("Clicked on Checkout button from Cart page")

        confirmPage.getCountryLocator().send_keys(confirmPage.countryText)
        self.verifyLinkPresence(confirmPage.countryName)
        countries = confirmPage.getCountriesList()
        for country in countries:
            countryText = (country.find_element(By.XPATH, 'ul/li').text).strip()
            if countryText == confirmPage.countryName:
                log.info("Select Country")
                country.find_element(By.XPATH, 'ul/li').click()
        confirmPage.getTermsAndConditions().click()
        log.info("Click on the purchase button")
        confirmPage.getPurchaseButton().click()
        successMsg = confirmPage.getSuccessMsgLocator().text
        assert confirmPage.expectedSuccessMsg in successMsg
        log.info("Code executed successfully and order is placed")
        log.info("Code executed successfully and order is placed 1234")
        log.info("Code executed successfully and order is placed 5678")

