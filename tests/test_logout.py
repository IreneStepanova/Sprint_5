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
    LOGOUT_BUTTON,
)
from conftest import BASE_URL


class TestLogout:

    def test_logout(self, driver, registered_user):
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

        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_HEADING)
        )
        assert driver.current_url == f"{BASE_URL}/login"
