from playwright.sync_api import Page
from pages.authorization import LoginPage


def test_user_can_login(page: Page):
    login_page = LoginPage(page)

    login_page.login("ki", "py")