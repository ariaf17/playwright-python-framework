from playwright.sync_api import Page, Locator, expect
from utils.logger import get_logger


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.log = get_logger(self.__class__.__name__)

        self.username: Locator = page.locator("#user-name")
        self.password: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error: Locator = page.locator("[data-test='error']")

    def navigate(self, base_url: str) -> None:
        self.log.info(f"Navigating to {base_url}")
        self.page.goto(base_url)

    def login(self, username: str, password: str) -> None:
        self.log.info(f"Logging in as '{username}'")
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def assert_error_contains(self, text: str) -> None:
        expect(self.error).to_contain_text(text)
    def assert_logged_in(self) -> None:
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")