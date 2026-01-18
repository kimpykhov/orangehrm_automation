def test_homepage_title(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    assert "OrangeHRM" in page.title()