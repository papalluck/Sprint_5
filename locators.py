from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы для элементов главной страницы
    """
    LOGIN_BUTTON = (By.XPATH, "//div/main/section[2]/div/button")  # Кнопка "Войти в аккаунт"
    REGISTER_LINK = (By.XPATH, "//div/main/div/div/p[1]/a")  # Ссылка "Зарегистрироваться"
    PERSONAL_CABINET_LINK = (By.XPATH, "//div/header/nav/a/p") # Ссылка "Личный кабинет"
    CONSTRUCTOR_LINK = (By.XPATH, "//div/header/nav/ul/li[1]/a/p") # Ссылка "Конструктор"
    LOGO_LINK = (By.XPATH, "//div/header/nav/div/a") # Логотип

class RegisterPageLocators:
    """
    Локаторы для элементов страницы регистрации
    """
    NAME_INPUT = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")  # Поле ввода "Имя"
    EMAIL_INPUT = (By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input")  # Поле ввода "Email"
    PASSWORD_INPUT = (By.XPATH, "//div/main/div/form/fieldset[3]/div/div/input")  # Поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//div/main/div/form/button")  # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE = (By.XPATH, "//div/main/div/form/fieldset[3]/div/p") # Сообщение об ошибке "Некорректный пароль"
    LOGIN_BUTTON_FROM_REGISTER_FORM = (By.XPATH, "//div / main / div / div / p / a") # Кнопка "Войти"
class LoginPageLocators:
    """
    Локаторы для элементов страницы входа
    """
    EMAIL_INPUT = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")  # Поле ввода "Email"
    PASSWORD_INPUT = (By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input")  # Поле ввода "Пароль"
    LOGIN_BUTTON = (By.XPATH, "//div/main/div/form/button")  # Кнопка "Войти"
    RESET_PASSWORD_LINK = (By.XPATH, "//div/main/div/div/p[2]/a") # Ссылка "Восстановить пароль"
    LOGIN_BUTTON_FROM_RECOVERY_FORM = (By.XPATH, "//div / main / div / div / p / a") # Кнопка "Войти" из формы "Восстановить пароль"

class ProfilePageLocators:
     """
    Локаторы для элементов личного кабинета
    """
     LOGOUT_BUTTON = (By.XPATH, "//div/main/div/nav/ul/li[3]/button") # Кнопка "Выйти"
     ACCOUNT_LINK = (By.XPATH, "//div/main/div/nav/ul/li[1]/a") # Кнопка "Профиль"

class ConstructorPageLocators:
    """
    Локаторы для элементов страницы конструктора
    """
    BUNS_TAB = (By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default' and text()='Булки']")  # Таб "Булки"
    SAUCES_TAB = (By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default' and text()='Соусы']")  # Таб "Соусы"
    FILLINGS_TAB = (By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default' and text()='Начинки']")  # Таб "Начинки"
    CURRENT_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[@class='text text_type_main-default']") # Текущий таб
    CHECKOUT_BUTTON = (By.XPATH, "//div / main / section[2] / div / button")  # Кнопка "Оформить заказ"
    CONSTRUCTOR_HEADER = (By.XPATH, "//div / main / section[1] / h1") # Заголовок "Соберите бургер"
