from playwright.sync_api import Page, Locator, expect
from utils.logger import get_logger
import re


class CheckoutInformationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.log = get_logger(self.__class__.__name__)

        self.first_name: Locator = page.locator("[data-test='firstName']")
        self.last_name: Locator = page.locator("[data-test='lastName']")
        self.postal_code: Locator = page.locator("[data-test='postalCode']")
        self.continue_button: Locator = page.locator("[data-test='continue']")
        self.error: Locator = page.locator("[data-test='error']")

    def assert_loaded(self) -> None:
        self.log.info("Asserting checkout info page loaded")
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-one\.html$"))

    def submit_info(self, first: str, last: str, zip_code: str) -> None:
        self.log.info("Submitting checkout information")
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def assert_error_contains(self, text: str) -> None:
        expect(self.error).to_contain_text(text)
