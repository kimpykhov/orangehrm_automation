from locators.authorization import LoginPageLocators
from config.config import BASE_URL

class LoginPage:
    def init(self, page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, page, username, password):
        self.page.fill(LoginPageLocators.USERNAME_INPUT, username)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, password)