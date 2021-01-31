from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomepageLocators:
    LOCATOR_MACBOOK = (
        By.XPATH,
        '//div[@class="product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12"]//a[text()="MacBook"]'
    )
    LOCATOR_IPHONE = (
        By.XPATH,
        '//div[@class="product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12"]//a[text()="iPhone"]'
    )
    LOCATOR_CANNON = (
        By.XPATH,
        '//div[@class="product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12"]//a[text()="Canon EOS 5D"]'
    )
    LOCATOR_MENU_COMPONENTS = (
        By.XPATH,
        '//ul[@class="nav navbar-nav"]//a[text()="Components"]'
    )
    LOCATOR_MENU_COMPONENTS_MONITOR = (
        By.XPATH,
        '//div[@class="dropdown-inner"]//a[@href="http://localhost/component/monitor"]'
    )
    LOCATOR_SEARCH_INPUT = (
        By.XPATH,
        '//input[@class="form-control input-lg"]'
    )


class HomepageHelper(BasePage):

    def go_to_macbook_page(self):
        macbook_good = self.find_element(HomepageLocators.LOCATOR_MACBOOK)
        macbook_good.click()
        current_url = self.driver.current_url
        template_url_text = 'http://localhost/macbook'
        assert template_url_text in current_url

