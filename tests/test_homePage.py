import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Entering FirstName... ")
        homePage.getName().send_keys(getData["firstName"])
        log.info("Entering Email...")
        homePage.getEmail().send_keys(getData["email"])
        log.info("Clicking on Checkbox...")
        homePage.getCheckBox().click()
        log.info("Selecting Gender...")
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()

        alertText = homePage.getSuccessMessage().text
        assert ("Success" in alertText)
        log.info("Form submitted successfully...")
        self.driver.refresh()
