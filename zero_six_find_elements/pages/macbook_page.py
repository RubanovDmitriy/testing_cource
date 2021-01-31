from selenium.webdriver.common.by import By
from .base_page import BasePage


class MacBookPageLocators:
    LOCATOR_MACBOOK_BREADCRUMB = (
        By.XPATH,
        '//ul[@class="breadcrumb"]//a[text()="MacBook"]'
    )


class MacBookPageHelper(BasePage):

    def check_breadcrumb_visibility(self):
        macbook_breadcrumb = self.find_element(MacBookPageLocators.LOCATOR_MACBOOK_BREADCRUMB)
        assert macbook_breadcrumb.is_displayed()
