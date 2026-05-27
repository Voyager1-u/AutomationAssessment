# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage


# class HomePage(BasePage):

#     signup_login_btn = (By.LINK_TEXT, "Signup / Login")
#     products_btn = (By.XPATH, "//a[@href='/products']")
#     cart_btn = (By.LINK_TEXT, "Cart")
#     delete_account_btn = (By.LINK_TEXT, "Delete Account")
#     logout_btn = (By.LINK_TEXT, "Logout")

#     def click_signup_login(self):
#         self.click_element(*self.signup_login_btn)

#     def click_products(self):
#         self.js_click(*self.products_btn)

#     def click_cart(self):
#         self.click_element(*self.cart_btn)
    
#     def click_delete_account(self):
#         self.click_element(*self.delete_account_btn)

#     def click_logout(self):
#         self.click_element(*self.logout_btn)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    signup_login_btn = (By.XPATH, "//a[contains(text(),'Signup / Login')]")

    products_btn = (By.XPATH, "//a[@href='/products']")

    delete_account_btn = (By.LINK_TEXT, "Delete Account")

    def click_signup_login(self):
        self.js_click(*self.signup_login_btn)

    def click_products(self):
        self.js_click(*self.products_btn)

    def click_delete_account(self):
        self.js_click(*self.delete_account_btn)

