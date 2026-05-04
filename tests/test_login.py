from pages.login_page import LoginPage
from utils.config import BASE_URL, EMAIL, PASSWORD
import pytest
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.parametrize("email, password, expected, valid",[
    (EMAIL, PASSWORD, "Logged in as", True),
    ("wrong@gmail.com" , "wrong123", "incorrect", False)
])
def test_login(driver, email, password, expected, valid):

    logger.info("Starting test_login..")
    logger.info("Opening application")
    driver.get(BASE_URL)
    login = LoginPage(driver)

    logger.info("Performing login flow")
    login.login(email, password)

    logger.info("Validating login result")
    if valid:
        assert expected in login.get_logged_in_text()
    else:
        assert expected in login.get_error_message()

