from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
import time
from utils.logger import get_logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger()
    
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        for i in range(3):  # retry mechanism
            element = self.find(locator)
            try:  
                element.click()
                return
            except ElementClickInterceptedException:
                time.sleep(1)
                self.driver.execute_script("arguments[0].click();", element)
                return
            except StaleElementReferenceException:
                continue
    
    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)
    
    def get_text(self, locator):
        return self.find(locator).text

    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    