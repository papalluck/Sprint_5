from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators,ProfilePageLocators,ConstructorPageLocators
from conftest import driver,loggined_driver


class TestTransferToYourPersonalAccount:
    def test_go_to_profile(self, loggined_driver):
        loggined_driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(loggined_driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))

        assert loggined_driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).is_displayed()

    def test_go_to_constructor_from_profile(self,loggined_driver):
        loggined_driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(loggined_driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
        loggined_driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()
        WebDriverWait(loggined_driver, 20).until(EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))

        assert loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).is_displayed()

    def test_go_to_constructor_from_profile_logo(self, loggined_driver):
        loggined_driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(loggined_driver, 20).until(EC.visibility_of_element_located(MainPageLocators.LOGO_LINK))
        loggined_driver.find_element(*MainPageLocators.LOGO_LINK).click()
        WebDriverWait(loggined_driver, 20).until(EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))

        assert loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).is_displayed()