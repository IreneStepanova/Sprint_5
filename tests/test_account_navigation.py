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
    CONSTRUCTOR_LINK,
    LOGO,
)
from conftest import BASE_URL


class TestAccountNavigation:

    def login(self, driver, registered_user):
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

    def test_go_to_personal_account(self, driver, registered_user):
        self.login(driver, registered_user)
        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )
        assert "/account" in driver.current_url

    def test_go_to_constructor_via_tab(self, driver, registered_user):
        self.login(driver, registered_user)
        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        driver.find_element(*CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PLACE_ORDER_BUTTON)
        )
        assert driver.current_url == f"{BASE_URL}/"

    def test_go_to_main_via_logo(self, driver, registered_user):
        self.login(driver, registered_user)
        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        driver.find_element(*LOGO).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PLACE_ORDER_BUTTON)
        )
        assert driver.current_url == f"{BASE_URL}/"
