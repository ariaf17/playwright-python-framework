from playwright.sync_api import Page, Locator, expect
from utils.logger import get_logger
import re


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.log = get_logger(self.__class__.__name__)

        self.checkout_button: Locator = page.locator("[data-test='checkout']")
        self.cart_items: Locator = page.locator(".cart_item")
        self.cart_link: Locator = page.locator(".shopping_cart_link")

    def open(self) -> None:
        self.log.info("Opening cart")
        self.cart_link.click()
        expect(self.page).to_have_url(re.compile(r".*/cart\.html$"))

    def assert_has_items(self) -> None:
        self.log.info("Asserting cart has at least 1 item")
        expect(self.cart_items.first).to_be_visible()

    def checkout(self) -> None:
        self.log.info("Clicking checkout")
        self.checkout_button.click()
