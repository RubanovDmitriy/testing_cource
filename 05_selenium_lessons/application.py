from selenium import webdriver
import argparse


class Application:
    def __init__(self, browser_name):
        self.browser = browser_name
        if self.browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            self.wd = webdriver.Firefox()

    def test_smth(self):
        self.wd.get("https://otus.ru/")
        phone_test = self.wd.find_elements_by_xpath(
            "//a[contains(@class, 'header2_subheader-link header2_subheader-link__phone')]"
        )[0].text
        return phone_test


parser = argparse.ArgumentParser()
parser.add_argument(
    "-wd",
    action="store",
    dest="wd",
    help="chrome to use chromedriver, or firefox to use geckodriver",
    type=str)
args = parser.parse_args()

application = Application(args.wd)
print(application.test_smth())
