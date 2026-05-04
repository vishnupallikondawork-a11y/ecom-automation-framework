from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import BASE_URL, EMAIL, PASSWORD
from utils.logger import get_logger

logger = get_logger()

def test_add_to_cart(driver):

    logger.info("Starting test_cart..")
    logger.info("Opening application")
    driver.get(BASE_URL)
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    # Login
    logger.info("Performing login flow")
    login.login(EMAIL, PASSWORD)

    # Product flow
    logger.info("Starting Add product to cart flow")
    product.add_product_to_cart()

    # Validation
    logger.info("validating cart items")
    items = cart.get_cart_items()
    assert len(items) > 0