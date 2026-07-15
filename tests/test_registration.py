from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    NAME_INPUT,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_BUTTON,
    LOGIN_HEADING,
)
from helpers import generate_email, generate_password, generate_name, generate_short_password
from conftest import BASE_URL


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(f"{BASE_URL}/register")

        driver.find_element(*NAME_INPUT).send_keys(generate_name())
        driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*PASSWORD_INPUT).send_keys(generate_password())

        driver.find_element(*REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_HEADING)
        )
        assert driver.current_url == f"{BASE_URL}/login"

    def test_registration_invalid_password(self, driver):
        driver.get(f"{BASE_URL}/register")

        driver.find_element(*NAME_INPUT).send_keys(generate_name())
        driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*PASSWORD_INPUT).send_keys(generate_short_password())

        driver.find_element(*REGISTER_BUTTON).click()

        assert driver.current_url != f"{BASE_URL}/login"
