from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def username_input(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    @property
    def password_input(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, "password")))

    @property
    def login_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    @property
    def dashboard_header(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
