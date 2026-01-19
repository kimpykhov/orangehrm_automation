from locators.authorization import LoginPageLocators
from config.config import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)