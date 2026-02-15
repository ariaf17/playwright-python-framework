from playwright.sync_api import Page, expect
from utils.logger import get_logger


class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.locator("h1")
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, base_url: str) -> None:
        self.logger.info(f"Navigating to {base_url}")
        self.page.goto(base_url)

    def assert_title(self, expected_title: str) -> None:
        self.logger.info(f"Asserting page title equals '{expected_title}'")
        expect(self.page).to_have_title(expected_title)

    def assert_heading(self, expected_heading: str) -> None:
        self.logger.info(f"Asserting heading equals '{expected_heading}'")
        expect(self.heading).to_have_text(expected_heading)
