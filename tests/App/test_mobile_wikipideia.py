import sys
import os
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


# Project root path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )
)

from utils.logger import get_logger


logger = get_logger("wiki_app_logs")


USERNAME = "uday_ftDZTA"
ACCESS_KEY = "QA5ZBr2zDdQHdykZ3uUS"


def test_wikipedia_app():

    logger.info("START: Wikipedia Mobile App Test")

    options = UiAutomator2Options()

    logger.info("Setting capabilities")

    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")

    options.set_capability("deviceName", "Samsung Galaxy S22")
    options.set_capability("platformVersion", "12.0")

    options.set_capability(
        "app",
        "bs://sample.app"
    )

    options.set_capability("project", "Automation Assessment")
    options.set_capability("build", "Wikipedia Build")
    options.set_capability("name", "Wikipedia App Test")

    logger.info("Connecting to BrowserStack")

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    logger.info("Application launched successfully")

    time.sleep(5)

    # Click search button
    logger.info("Finding Search Wikipedia button")

    search_button = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Search Wikipedia"
    )

    logger.info("Clicking search button")

    search_button.click()

    time.sleep(2)

    # Enter search text
    logger.info("Finding search input field")

    search_input = driver.find_element(
        AppiumBy.ID,
        "org.wikipedia.alpha:id/search_src_text"
    )

    logger.info("Entering text: BrowserStack")

    search_input.send_keys("BrowserStack")

    time.sleep(3)

    logger.info("Validating search result")

    page_source = driver.page_source

    assert "BrowserStack" in page_source

    logger.info("Validation successful")

    print("Wikipedia search successful")

    logger.info("Closing application")

    driver.quit()

    logger.info("END: Wikipedia Mobile App Test PASSED")