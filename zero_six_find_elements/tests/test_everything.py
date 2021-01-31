from zero_six_find_elements.pages.homepage import HomepageHelper
from zero_six_find_elements.pages.macbook_page import MacBookPageHelper


def test_macbook_page_redirect(browser):
    homepage = HomepageHelper(browser)
    macbook_page = MacBookPageHelper(browser)
    homepage.go_to_site()
    homepage.go_to_macbook_page()
    macbook_page.check_breadcrumb_visibility()
