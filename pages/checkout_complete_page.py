from playwright.sync_api import Page, Locator, expect
from utils.logger import get_logger
import re


class CheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.log = get_logger(self.__class__.__name__)

        self.complete_header: Locator = page.locator(".complete-header")

    def assert_loaded(self) -> None:
        self.log.info("Asserting checkout complete page loaded")
        expect(self.page).to_have_url(re.compile(r".*/checkout-complete\.html$"))
        

    def assert_success_message(self) -> None:
        expect(self.complete_header).to_have_text("Thank you for your order!")
