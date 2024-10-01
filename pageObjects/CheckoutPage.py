from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    product_name = "Blackberry" # to use reg Xpath "//a[contains(@href, 'shop')]
    allProducts = (By.CSS_SELECTOR, ".card")
    productNameFromPage = (By.XPATH, "div/h4/a")
    ckeckOutButton = (By.CSS_SELECTOR, ".btn-primary")
    productAddedInCart = (By.XPATH, '(//h4[@class="media-heading"])[1]/a')
    cartPageCheckoutButton = (By.CSS_SELECTOR, '.btn-success')

    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.allProducts)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.ckeckOutButton)

    def getProductAddedInCart(self):
        return self.driver.find_element(*CheckOutPage.productAddedInCart)

    def getCartPageCheckoutButton(self):
        self.driver.find_element(*CheckOutPage.cartPageCheckoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
