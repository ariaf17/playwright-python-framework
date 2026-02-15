import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_login_success(page, base_url, sauce_username, sauce_password):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login(sauce_username, sauce_password)

    inv = InventoryPage(page)
    inv.assert_loaded()


@pytest.mark.smoke
def test_login_locked_out_user_shows_error(page, base_url, sauce_password):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login("locked_out_user", sauce_password)
    login.assert_error_contains("locked out")
