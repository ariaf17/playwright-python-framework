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
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")


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

    def sort_by_visible_text(self, option_text: str) -> None:
        self.log.info(f"Sorting by: {option_text}")
        self.sort_dropdown.select_option(label=option_text)

    def get_all_item_names(self) -> list[str]:
        names = [n.strip() for n in self.item_names.all_inner_texts()]
        self.log.info(f"Captured {len(names)} item names")
        return names

    def get_all_item_prices(self) -> list[float]:
        raw = [p.strip() for p in self.item_prices.all_inner_texts()]
        prices = [float(x.replace("$", "")) for x in raw]
        self.log.info(f"Captured {len(prices)} item prices")
        return prices

