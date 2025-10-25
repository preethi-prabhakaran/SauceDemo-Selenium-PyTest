from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# currently, supports only chrome browser

def create_driver(browser="chrome", headless = True):
    if browser == "chrome":
        options = Options()

        # Disable password manager and save prompts, to avoid some unnecessary popups related to password leak
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,  # Disable notifications
            "autofill.profile_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # Additional arguments for blocking popups in chrome while test run
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=Autofill,PasswordManagerOnboarding")

        # Arguments for docker run
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=9222")

        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    return driver