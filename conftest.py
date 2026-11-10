from pathlib import Path

import pytest

from pages.login_page import LoginPage
from utils.driver_factory import create_driver

SCREENSHOT_DIR = Path(__file__).parent / "reports" / "screenshots"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="chrome or firefox")
    parser.addoption("--headless", action="store_true", help="run the browser without a window")


@pytest.fixture
def driver(request):
    kwargs = {}
    if request.config.getoption("--browser"):
        kwargs["browser"] = request.config.getoption("--browser")
    if request.config.getoption("--headless"):
        kwargs["headless"] = True

    browser = create_driver(**kwargs)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).open()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "driver" in item.fixturenames:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        item.funcargs["driver"].save_screenshot(str(SCREENSHOT_DIR / f"{item.name}.png"))
