from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    # LOCATORS
    CART_ITEMS = (By.XPATH, "//tr[contains(@id,'product')]")

    # ACTIONS
    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)
    