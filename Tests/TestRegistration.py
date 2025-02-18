import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
from conftest import driver,loggined_driver


class TestRegistration:
    def test_successful_registration(self, driver):

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()


        driver.find_element(*MainPageLocators.REGISTER_LINK).click()


        name = "Владислав"
        email = f"VladislavZhurov15{random.randint(100, 999)}@yandex.ru"

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(
            Data.password)


        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()


        WebDriverWait(driver, Data.Wait_time).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)


        assert login_button.is_displayed()

    def test_registration_incorrect_password(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        driver.find_element(*MainPageLocators.REGISTER_LINK).click()
        name = "TestUser"
        email = f"VladislavZhurov15{random.randint(100, 999)}@yandex.ru"
        password = f"{random.randint(1, 99999)}"

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()


        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
        )

        message_error = driver.find_element(*RegisterPageLocators.ERROR_MESSAGE)

        assert message_error.is_displayed()