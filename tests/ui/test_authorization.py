from playwright.sync_api import Page
from pages.authorization import LoginPage
from playwright.sync_api import expect


def test_user_can_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login("ki", "py")

    expect(page).to_have_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    expect(page).to_have_title("OrangeHRM")