from selenium import webdriver

from config import settings


def create_driver(browser=settings.BROWSER, headless=settings.HEADLESS):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            # CI machines have no screen, and Chrome needs these flags inside containers.
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={settings.WINDOW_SIZE}")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        width, height = settings.WINDOW_SIZE.split(",")
        driver.set_window_size(int(width), int(height))
        return driver

    raise ValueError(f"Unsupported browser: {browser}")
