import pytest

VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"

# pytest's equivalent of TestNG's @DataProvider: each pytest.param is one test run.
LOGIN_CASES = [
    pytest.param(VALID_USERNAME, VALID_PASSWORD, "You logged into a secure area!", "/secure", id="valid_login"),
    pytest.param(VALID_USERNAME, "wrong-password", "Your password is invalid!", "/login", id="wrong_password"),
    pytest.param("wronguser", VALID_PASSWORD, "Your username is invalid!", "/login", id="wrong_username"),
]
