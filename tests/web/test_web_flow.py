import time

from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_web_flow():

    driver = get_driver()

    driver.get("https://automationexercise.com/")

    home = HomePage(driver)
    signup = SignupPage(driver)
    login = LoginPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # REGISTER USER
    home.click_signup_login()

    email = f"test{int(time.time())}@gmail.com"

    signup.register_user("Uday", email)

    # VALIDATE ACCOUNT CREATED
    assert "ACCOUNT CREATED!" in signup.validate_account_created()

    # CLICK CONTINUE
    signup.click_continue()

    # VALIDATE LOGIN
    assert "Logged in as" in login.validate_login()

    # GO TO PRODUCTS PAGE
    home.click_products()

    # ADD PRODUCT TO CART
    cart.add_product_to_cart()

    # VIEW CART
    cart.view_cart_page()

    # VALIDATE PRODUCT ADDED
    assert len(cart.validate_cart_product()) > 0

    # PROCEED TO CHECKOUT
    cart.checkout()

    # VALIDATE ADDRESS
    assert "Hyderabad" in checkout.validate_address()

    # DELETE ACCOUNT
    driver.get("https://automationexercise.com/")

    home.click_delete_account()

    driver.quit()