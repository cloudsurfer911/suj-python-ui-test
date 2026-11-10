import os

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com").rstrip("/")
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = bool(os.getenv("CI") or os.getenv("HEADLESS"))
TIMEOUT = int(os.getenv("TIMEOUT", "10"))
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1280,720")
