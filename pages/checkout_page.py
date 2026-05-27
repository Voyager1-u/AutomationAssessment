from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    address_details = (By.XPATH, "//ul[@id='address_delivery']")

    def validate_address(self):

        return self.get_text(*self.address_details)