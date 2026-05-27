from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):

    name_input = (By.NAME, "name")
    email_input = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

    password_input = (By.ID, "password")
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address = (By.ID, "address1")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")

    create_account_btn = (By.XPATH, "//button[@data-qa='create-account']")

    account_created = (By.XPATH, "//b[text()='Account Created!']")

    continue_btn = (By.XPATH, "//a[@data-qa='continue-button']")

    def register_user(self, name, email):

        self.enter_text(*self.name_input, name)
        self.enter_text(*self.email_input, email)

        self.click_element(*self.signup_btn)

        self.enter_text(*self.password_input, "Test@123")
        self.enter_text(*self.first_name, "Uday")
        self.enter_text(*self.last_name, "Tester")
        self.enter_text(*self.address, "Hyderabad")
        self.enter_text(*self.state, "Telangana")
        self.enter_text(*self.city, "Hyderabad")
        self.enter_text(*self.zipcode, "500001")
        self.enter_text(*self.mobile, "9876543210")

        self.js_click(*self.create_account_btn)

    def validate_account_created(self):
        return self.get_text(*self.account_created).strip()
    
    def click_continue(self):
        self.js_click(*self.continue_btn)