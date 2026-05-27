from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        ).click()

    def enter_text(self, by, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, locator))
        ).send_keys(text)

    def get_text(self, by, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, locator))
        ).text
    def js_click(self, by, locator):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, locator))
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )