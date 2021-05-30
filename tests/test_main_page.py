import time

from pages.locators import MainPageLocators, LoginPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    time.sleep(5)


def test_guest_should_see_login_link(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    link_login = LoginPageLocators.LINK
    time.sleep(5)
    pageLogin = LoginPage(browser, link_login)
    pageLogin.should_be_login_page()



