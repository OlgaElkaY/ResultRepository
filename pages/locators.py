from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_EMAIL_ADDRESS = (By.ID, 'id_login-username')
    LOGIN_PW = (By.ID, 'id_login - password')
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_ADDRESS = (By.ID, 'id_registration-email')
    REGISTER_PW = (By.ID, 'id_registration-password1')
    CONFIRM_PW = (By.ID, 'id_registration-password2')
    CONFIRM_BUTTON = (By.NAME, 'registration_submit')
