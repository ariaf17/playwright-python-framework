from playwright.sync_api import Page, Locator, expect
from utils.logger import get_logger
import re


class CheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.log = get_logger(self.__class__.__name__)

        self.finish_button: Locator = page.locator("[data-test='finish']")
        self.summary: Locator = page.locator(".summary_info")

        self.item_prices: Locator = page.locator(".inventory_item_price")
        self.summary_subtotal: Locator = page.locator(".summary_subtotal_label")
        self.summary_tax: Locator = page.locator(".summary_tax_label")
        self.summary_total: Locator = page.locator(".summary_total_label")


    def assert_loaded(self) -> None:
        self.log.info("Asserting checkout overview loaded")
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-two\.html$"))
        expect(self.summary).to_be_visible()

    def finish(self) -> None:
        self.log.info("Finishing checkout")
        self.finish_button.click()

    def get_item_prices(self) -> list[float]:
        raw = [p.strip() for p in self.item_prices.all_inner_texts()]
        return [float(x.replace("$", "")) for x in raw]

    def get_subtotal(self) -> float:
        text = self.summary_subtotal.inner_text()
        return float(text.split("$")[1])

    def get_tax(self) -> float:
        text = self.summary_tax.inner_text()
        return float(text.split("$")[1])

    def get_total(self) -> float:
        text = self.summary_total.inner_text()
        return float(text.split("$")[1])

