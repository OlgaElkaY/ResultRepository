from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, how, what):
        try:
            if how == 'css selector':
                element = self.browser.find_element_by_css_selector(what)
            else:
                element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return None
        return element