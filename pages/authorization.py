from locators.authorization import LoginPageLocators
from config.config import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill(LoginPageLocators.USERNAME_INPUT, username)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)
