import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import generate_email, generate_password, generate_name

BASE_URL = "https://stellarburgers.education-services.ru"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    # Генерируем данные нового пользователя
    email = generate_email()
    password = generate_password()
    name = generate_name()

    # Регистрируем пользователя через API
    resp = requests.post(
        f"{BASE_URL}/api/auth/register",
        json={"email": email, "password": password, "name": name},
    )
    body = resp.json()

    data = {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": body.get("accessToken", ""),
    }

    yield data

    # После теста удаляем пользователя
    if data["accessToken"]:
        requests.delete(
            f"{BASE_URL}/api/auth/user",
            headers={"Authorization": data["accessToken"]},
        )
