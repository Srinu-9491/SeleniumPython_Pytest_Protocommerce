from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryText = "ind"
    countryName = "India"
    countryLocator = (By.ID, 'country')
    countryList = (By.CSS_SELECTOR, '.suggestions')
    termsAndConditions = (By.CSS_SELECTOR, '.checkbox')
    purchaseButton = (By.CSS_SELECTOR, '.btn-success')
    successMsgLocator = (By.CSS_SELECTOR, '.alert-success')
    expectedSuccessMsg = "Success! Thank you! Your order will be delivered in next few weeks"

    def getCountryLocator(self):
        return self.driver.find_element(*ConfirmPage.countryLocator)

    def getCountriesList(self):
        return self.driver.find_elements(*ConfirmPage.countryList)

    def getTermsAndConditions(self):
        return self.driver.find_element(*ConfirmPage.termsAndConditions)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMsgLocator(self):
        return self.driver.find_element(*ConfirmPage.successMsgLocator)
