import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_add_to_cart_increments_badge(authenticated_page):
    page = authenticated_page
    inv = InventoryPage(page)

    inv.add_item_by_name("Sauce Labs Backpack")
    inv.assert_cart_count(1)
