from selenium.webdriver.common.by import By 
from pages.base_page import BasePage

class ProductPage(BasePage):

    #LOCATORS
    PRODUCTS_LINK = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
    FIRST_PRODUCT_ADD = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")
    VIEW_CART = (By.XPATH, "//u[text()='View Cart']")

    # ACTIONS
    def go_to_products(self):
        self.click(self.PRODUCTS_LINK)

    def add_first_product_to_cart(self):
        self.scroll_to_element(self.FIRST_PRODUCT_ADD)
        self.click(self.FIRST_PRODUCT_ADD)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def go_to_cart(self):
        self.click(self.VIEW_CART)

    # FUNCTIONS

    def add_product_to_cart(self):

        self.logger.info("Clicking products link...")
        self.go_to_products()

        self.logger.info("Adding product to cart")
        self.add_first_product_to_cart()

        self.logger.info("Opening cart")
        self.go_to_cart()
    

