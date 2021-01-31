from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomepageLocators:
    LOCATOR_SORT_BY_DROPDONW = (
        By.XPATH,
        '//select[@id="input-sort"]'
    )
    LOCATOR_SHOW_DROPDOWN = (
        By.XPATH,
        '//select[@id="input-limit"]'
    )


class SearchHelper(BasePage):
    pass
