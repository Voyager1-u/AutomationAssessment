

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

from pages.base_page import BasePage


class CartPage(BasePage):

    first_product = (
        By.XPATH,
        "(//a[contains(@class,'add-to-cart')])[1]"
    )

    view_cart_button = (
        By.XPATH,
        "//u[text()='View Cart']"
    )

    cart_products = (
        By.XPATH,
        "//tr[contains(@id,'product')]"
    )

    checkout_button = (
        By.XPATH,
        "//a[contains(text(),'Proceed To Checkout')]"
    )

    def add_product_to_cart(self):

        # Scroll down
        self.driver.execute_script(
            "window.scrollBy(0, 500);"
        )

        time.sleep(2)

        # Wait for clickable product
        product = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                self.first_product
            )
        )

        # Move to product
        ActionChains(self.driver).move_to_element(
            product
        ).perform()

        time.sleep(2)

        # JavaScript click
        self.driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(2)

    def view_cart_page(self):

        self.click_element(
            *self.view_cart_button
        )

    def validate_cart_product(self):

        return self.driver.find_elements(
            *self.cart_products
        )

    def checkout(self):

        self.click_element(
            *self.checkout_button
        )