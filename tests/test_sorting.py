import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_sort_name_a_to_z(authenticated_page):
    page = authenticated_page
    inv = InventoryPage(page)

    inv.sort_by_visible_text("Name (A to Z)")
    names = inv.get_all_item_names()

    assert names == sorted(names), "Names are not sorted A→Z"


@pytest.mark.regression
def test_sort_name_z_to_a(authenticated_page):
    page = authenticated_page
    inv = InventoryPage(page)

    inv.sort_by_visible_text("Name (Z to A)")
    names = inv.get_all_item_names()

    assert names == sorted(names, reverse=True), "Names are not sorted Z→A"


@pytest.mark.regression
def test_sort_price_low_to_high(authenticated_page):
    page = authenticated_page
    inv = InventoryPage(page)

    inv.sort_by_visible_text("Price (low to high)")
    prices = inv.get_all_item_prices()

    assert prices == sorted(prices), "Prices are not sorted low→high"
