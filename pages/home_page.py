from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.locator("h1")

    def navigate(self, base_url: str) -> None:
        self.page.goto(base_url)

    def assert_title(self) -> None:
        expect(self.page).to_have_title("Example Domain")

    def assert_heading(self) -> None:
        expect(self.heading).to_have_text("Example Domain")
