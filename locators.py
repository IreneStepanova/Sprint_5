from selenium.webdriver.common.by import By

# === Главная страница ===
# Кнопка «Войти в аккаунт» для неавторизованного пользователя
LOGIN_MAIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
# Кнопка «Оформить заказ» для авторизованного пользователя
PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
# Ссылка «Личный Кабинет» в хедере
PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
# Ссылка «Конструктор» в хедере
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")
# Логотип Stellar Burgers в хедере
LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")

# Табы конструктора
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::*")
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::*")
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::*")

# === Страница входа /login ===
# Заголовок «Вход»
LOGIN_HEADING = (By.XPATH, "//h2[text()='Вход']")
# Поле ввода Email (метка внутри компонента Input)
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
# Поле ввода пароля
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
# Кнопка «Войти»
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
# Ссылка «Зарегистрироваться» на странице входа
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
# Ссылка «Восстановить пароль» на странице входа
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

# === Страница регистрации /register ===
# Поле ввода имени (метка «Имя» внутри компонента Input)
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
# Кнопка «Зарегистрироваться»
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
# Ссылка «Войти» на странице регистрации
LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
# Ошибка «Такой пользователь уже существует»
REGISTER_ERROR = (By.XPATH, "//p[contains(text(),'Такой пользователь уже существует')]")

# === Страница восстановления пароля /forgot-password ===
# Заголовок «Восстановление пароля»
FORGOT_PASSWORD_HEADING = (By.XPATH, "//h2[text()='Восстановление пароля']")

# === Личный кабинет /account/profile ===
# Кнопка «Выход» в боковом меню
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
# Ссылка «Профиль» в боковом меню
PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
