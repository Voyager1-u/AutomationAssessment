from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")

    logged_in_text = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def login(self, email, password):

        self.enter_text(*self.login_email, email)
        self.enter_text(*self.login_password, password)

        self.click_element(*self.login_button)

    def validate_login(self):
        return self.get_text(*self.logged_in_text)