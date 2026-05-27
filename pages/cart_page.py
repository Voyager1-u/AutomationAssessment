from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    first_product = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")

    continue_shopping = (
        By.XPATH,
        "//button[text()='Continue Shopping']"
    )

    view_cart = (By.XPATH, "//u[text()='View Cart']")

    cart_product = (By.XPATH, "//td[@class='cart_description']/h4/a")

    proceed_checkout = (By.XPATH, "//a[text()='Proceed To Checkout']")

    def add_product_to_cart(self):

        self.click_element(*self.first_product)

    def view_cart_page(self):

        self.click_element(*self.view_cart)

    def validate_cart_product(self):

        return self.get_text(*self.cart_product)

    def checkout(self):

        self.click_element(*self.proceed_checkout)