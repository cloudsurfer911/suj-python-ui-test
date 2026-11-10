import pytest

from test_data.login_data import LOGIN_CASES


@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_message, expected_path", LOGIN_CASES)
def test_login(login_page, username, password, expected_message, expected_path):
    login_page.login(username, password)

    assert expected_message in login_page.flash_message()
    assert login_page.current_path == expected_path
