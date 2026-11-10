from pages.login_page import LoginPage


def test_login_with_valid_credentials(driver):
    page = LoginPage(driver).open()
    page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in page.flash_message()
    assert driver.current_url.endswith("/secure")


def test_login_with_wrong_password(driver):
    page = LoginPage(driver).open()
    page.login("tomsmith", "wrong-password")

    assert "Your password is invalid!" in page.flash_message()
    assert driver.current_url.endswith("/login")
