import pytest
from selenium import webdriver


# -----------------------------
# Web Driver Fixture
# -----------------------------
@pytest.fixture(scope="function")
def get_driver():
    print("\nLaunching Chrome Browser")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    print("\nClosing Browser")
    driver.quit()


# -----------------------------
# Sample API Base URL Fixture
# -----------------------------
@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"