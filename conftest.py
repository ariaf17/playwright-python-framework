from pathlib import Path
import pytest

from utils.config import BASE_URL, SAUCE_USERNAME, SAUCE_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def sauce_username() -> str:
    return SAUCE_USERNAME


@pytest.fixture(scope="session")
def sauce_password() -> str:
    return SAUCE_PASSWORD


def pytest_configure(config: pytest.Config) -> None:
    Path("reports/screenshots").mkdir(parents=True, exist_ok=True)
    Path("reports/traces").mkdir(parents=True, exist_ok=True)


@pytest.fixture
def authenticated_page(page, base_url: str, sauce_username: str, sauce_password: str):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login(sauce_username, sauce_password)

    inv = InventoryPage(page)
    inv.assert_loaded()
    return page
