import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    # GitHub Actions sets CI=true; there is no screen there, so Chrome must run headless.
    if os.getenv("CI") or os.getenv("HEADLESS"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,720")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
