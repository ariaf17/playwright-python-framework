import re

import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from utils.config import BASE_URL
from utils.data_loader import load_test_data

test_data = load_test_data("home_test_data.json")


@pytest.mark.smoke
@pytest.mark.parametrize("case", test_data)
def test_homepage_title(page, base_url, case):
    home = HomePage(page)
    home.navigate(base_url)
    home.assert_title(case["expected_title"])
    home.assert_heading(case["expected_heading"])

