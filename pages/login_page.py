from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    #LOCATORS
    LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'incorrect')]")


    # ACTIONS
    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_logged_in_text(self):
        return self.get_text(self.LOGGED_IN_TEXT)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    #FUNCTIONS

    def login(self, email, password):
        self.logger.info("Clicking login link")
        self.click_login_link()

        self.logger.info(f"Entering email: {email}")
        self.enter_email(email)

        self.logger.info("Entering password")
        self.enter_password(password)

        self.logger.info("Clicking login button")
        self.click_login()

