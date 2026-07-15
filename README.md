# Stellar Burgers — автотесты

Набор автотестов для сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/).

## Технологии

- Python 3.10+
- pytest
- Selenium WebDriver (Google Chrome)
- webdriver-manager
- requests

## Структура проекта

```
├── conftest.py                  # Фикстуры: driver, registered_user, logged_in_browser
├── helpers.py                   # Генераторы email, пароля, имени
├── locators.py                  # Локаторы элементов на всех страницах
├── requirements.txt             # Зависимости
├── .gitignore
└── tests/
    ├── test_registration.py     # Регистрация (2 теста)
    ├── test_login.py            # Вход через 4 точки входа (4 теста)
    ├── test_account_navigation.py  # Переходы в ЛК и обратно (3 теста)
    ├── test_logout.py           # Выход из аккаунта (1 тест)
    └── test_constructor.py      # Переходы по табам конструктора (3 теста)
```

## Запуск

```bash
pip install -r requirements.txt
python3 -m pytest tests/
```

## Тест-кейсы

### Регистрация
- **test_registration_success** — успешная регистрация с валидными данными, проверка перехода на `/login`
- **test_registration_invalid_password** — регистрация с паролем короче 6 символов, проверка что страница не изменилась

### Вход
- **test_login_from_main_button** — вход через кнопку «Войти в аккаунт» на главной
- **test_login_from_personal_account** — вход через кнопку «Личный кабинет»
- **test_login_from_registration_form** — вход через ссылку «Войти» в форме регистрации
- **test_login_from_password_recovery** — вход через ссылку «Войти» в форме восстановления пароля

### Личный кабинет
- **test_go_to_personal_account** — переход в личный кабинет по клику на «Личный кабинет»
- **test_go_to_constructor_via_tab** — переход из ЛК в конструктор через «Конструктор»
- **test_go_to_main_via_logo** — переход из ЛК на главную через логотип

### Выход
- **test_logout** — выход по кнопке «Выйти» в личном кабинете

### Конструктор
- **test_buns_tab** — переключение на таб «Булки»
- **test_sauces_tab** — переключение на таб «Соусы»
- **test_fillings_tab** — переключение на таб «Начинки»
