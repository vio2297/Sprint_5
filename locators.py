from selenium.webdriver.common.by import By

# Форма регистрации
class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")  # Поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке
    ERROR_MESSAGE_REG_NAME_EMPTY = (By.XPATH, ".//p[text() = 'Заполните поле ИМЯ']")  # ошибка при пустом поле Имя
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти"

# Авторизация
class AuthorizationLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")  # Поле "Пароль"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Ошибка при неверных данных
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка на регистрацию
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка на восстановление пароля

# Главная страница
class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers

# Личный кабинет
class AccountPageLocators:
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")  # Заголовок "Профиль"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выйти"

# Конструктор
class ConstructorLocators:
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Раздел "Начинки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Раздел "Булки"


