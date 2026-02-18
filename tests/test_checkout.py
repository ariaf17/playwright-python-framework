import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.regression
def test_checkout_happy_path(authenticated_page):
    page = authenticated_page

    inv = InventoryPage(page)
    inv.add_item_by_name("Sauce Labs Backpack")
    inv.assert_cart_count(1)

    cart = CartPage(page)
    cart.open()
    cart.assert_has_items()
    cart.checkout()

    info = CheckoutInformationPage(page)
    info.assert_loaded()
    info.submit_info("Aria", "Test", "SW1A1AA")

    overview = CheckoutOverviewPage(page)
    overview.assert_loaded()
    prices = overview.get_item_prices()
    subtotal = overview.get_subtotal()
    tax = overview.get_tax()
    total = overview.get_total()

    expected_subtotal = sum(prices)
    expected_total = round(expected_subtotal + tax, 2)

    assert subtotal == expected_subtotal, "Subtotal mismatch"
    assert round(total, 2) == expected_total, "Total mismatch"

    overview.finish()

    complete = CheckoutCompletePage(page)
    complete.assert_loaded()
    complete.assert_success_message()


@pytest.mark.regression
def test_checkout_requires_postal_code(authenticated_page):
    page = authenticated_page

    inv = InventoryPage(page)
    inv.add_item_by_name("Sauce Labs Backpack")

    cart = CartPage(page)
    cart.open()
    cart.checkout()

    info = CheckoutInformationPage(page)
    info.assert_loaded()
    info.submit_info("Aria", "Test", "")  # missing zip
    info.assert_error_contains("Postal Code is required")

@pytest.mark.regression
def test_checkout_requires_first_name(authenticated_page):
    page = authenticated_page

    inv = InventoryPage(page)
    inv.add_item_by_name("Sauce Labs Backpack")

    cart = CartPage(page)
    cart.open()
    cart.checkout()

    info = CheckoutInformationPage(page)
    info.assert_loaded()
    info.submit_info("", "Test", "SW1A1AA")  # missing first name
    info.assert_error_contains("First Name is required")

