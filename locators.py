from selenium.webdriver.common.by import By

class Locators:
    # Форма регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    ERROR_MESSAGE_REG_NAME_EMPTY = (By.XPATH, "//p[text()='Заполните поле ИМЯ']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Авторизация
    LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, 'login')]//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//form[contains(@class, 'login')]//p[@class='input__error text_type_main-default']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    LOGIN_TEXT_LINK = (By.XPATH, "//a[text()='Войти']")

    # Навигация
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_logo')]")
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Конструктор
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//*[text()='Соберите бургер']")
    SERVICE_LOGO_BUTTON = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")
