import re

import pytest
from playwright.sync_api import Page, expect
from utils.config import BASE_URL


@pytest.mark.smoke
def test_homepage_title(page: Page) -> None:
    page.goto(BASE_URL)
    expect(page).to_have_title(re.compile("Example Domain"))
    expect(page.locator("h1")).to_have_text("Example Domain")
