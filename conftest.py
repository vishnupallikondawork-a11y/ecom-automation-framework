import pytest
from selenium import webdriver
import os
from datetime import datetime
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed: 
        driver = item.funcargs['driver']

        # create screenshots folder
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # unique name
        test_name = item.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"screenshots/{test_name}_{timestamp}.png"

        driver.save_screenshot(file_name)