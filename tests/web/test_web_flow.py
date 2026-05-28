
import sys
import os
import time


# Project root path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )
)

from utils.logger import get_logger

from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


logger = get_logger("web_automation_logs")


def test_complete_web_flow():

    logger.info("START: Web Automation Flow Test")

    logger.info("Launching browser")

    driver = get_driver()

    logger.info("Opening Automation Exercise website")

    driver.get("https://automationexercise.com/")

    home = HomePage(driver)
    signup = SignupPage(driver)
    login = LoginPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # REGISTER USER
    logger.info("Navigating to Signup/Login page")

    home.click_signup_login()

    email = f"test{int(time.time())}@gmail.com"

    logger.info(f"Generated Email: {email}")

    logger.info("Registering new user")

    signup.register_user("Uday", email)

    logger.info("Validating account creation")

    assert "ACCOUNT CREATED!" in signup.validate_account_created()

    logger.info("Account created successfully")

    # CLICK CONTINUE
    logger.info("Clicking Continue button")

    signup.click_continue()

    # VALIDATE LOGIN
    logger.info("Validating user login")

    assert "Logged in as" in login.validate_login()

    logger.info("Login successful")

    # GO TO PRODUCTS PAGE
    logger.info("Navigating to Products page")

    home.click_products()

    # ADD PRODUCT TO CART
    logger.info("Adding product to cart")

    cart.add_product_to_cart()

    # VIEW CART
    logger.info("Opening cart page")

    cart.view_cart_page()

    # VALIDATE PRODUCT ADDED
    logger.info("Validating cart product")

    assert len(cart.validate_cart_product()) > 0

    logger.info("Product added to cart successfully")

    # PROCEED TO CHECKOUT
    logger.info("Proceeding to checkout")

    cart.checkout()

    # VALIDATE ADDRESS
    logger.info("Validating checkout address")

    assert "Hyderabad" in checkout.validate_address()

    logger.info("Address validation successful")

    # DELETE ACCOUNT
    logger.info("Navigating back to homepage")

    driver.get("https://automationexercise.com/")

    logger.info("Deleting created account")

    home.click_delete_account()

    logger.info("Closing browser")

    driver.quit()

    logger.info("END: Web Automation Flow Test PASSED")