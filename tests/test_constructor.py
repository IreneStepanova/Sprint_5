from selenium.webdriver.support.wait import WebDriverWait
from locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB
from conftest import BASE_URL


class TestConstructor:

    def test_buns_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SAUCES_TAB).click()
        WebDriverWait(driver, 3).until(
            lambda d: "current" in d.find_element(*SAUCES_TAB).get_attribute("class")
        )

        driver.find_element(*BUNS_TAB).click()
        WebDriverWait(driver, 3).until(
            lambda d: "current" in d.find_element(*BUNS_TAB).get_attribute("class")
        )

    def test_sauces_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SAUCES_TAB).click()
        WebDriverWait(driver, 3).until(
            lambda d: "current" in d.find_element(*SAUCES_TAB).get_attribute("class")
        )

    def test_fillings_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*FILLINGS_TAB).click()
        WebDriverWait(driver, 3).until(
            lambda d: "current" in d.find_element(*FILLINGS_TAB).get_attribute("class")
        )
