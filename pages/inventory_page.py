from playwright.sync_api import Page, Locator, expect
from utils.logger import get_logger


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.log = get_logger(self.__class__.__name__)

        self.title: Locator = page.locator(".title")
        self.inventory_container: Locator = page.locator("[data-test='inventory-container']")
        self.cart_badge: Locator = page.locator(".shopping_cart_badge")
        self.cart_link: Locator = page.locator(".shopping_cart_link")

    def assert_loaded(self) -> None:
        self.log.info("Asserting inventory page loaded")
        expect(self.inventory_container).to_be_visible()
        expect(self.title).to_have_text("Products")

    def add_item_by_name(self, item_name: str) -> None:
        self.log.info(f"Adding item to cart: {item_name}")
        item = self.page.locator(".inventory_item").filter(has_text=item_name)
        expect(item).to_have_count(1)
        item.get_by_role("button", name="Add to cart").click()

    def assert_cart_count(self, count: int) -> None:
        if count == 0:
            expect(self.cart_badge).to_have_count(0)
        else:
            expect(self.cart_badge).to_have_text(str(count))
    def go_to_cart(self) -> None:
        self.log.info("Navigating to cart page")
        self.cart_link.click()