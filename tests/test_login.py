from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    LOGIN_MAIN_BUTTON,
    LOGIN_HEADING,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    PLACE_ORDER_BUTTON,
    PERSONAL_ACCOUNT_LINK,
    LOGIN_LINK,
)
from conftest import BASE_URL


class TestLogin:

    def test_login_from_main_button(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_HEADING)
        )

        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PLACE_ORDER_BUTTON)
        )
        assert driver.current_url == f"{BASE_URL}/"

    def test_login_from_personal_account(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_HEADING)
        )

        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PLACE_ORDER_BUTTON)
        )
        assert driver.current_url == f"{BASE_URL}/"

    def test_login_from_registration_form(self, driver, registered_user):
        driver.get(f"{BASE_URL}/register")
        driver.find_element(*LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_HEADING)
        )

        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PLACE_ORDER_BUTTON)
        )
        assert driver.current_url == f"{BASE_URL}/"

    def test_login_from_password_recovery(self, driver, registered_user):
        driver.get(f"{BASE_URL}/forgot-password")
        driver.find_element(*LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_HEADING)
        )

        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PLACE_ORDER_BUTTON)
        )
        assert driver.current_url == f"{BASE_URL}/"
