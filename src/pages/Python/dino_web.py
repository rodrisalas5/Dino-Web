from selenium.webdriver.common.by import By
import time


class DinoWebPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = None
        self.browser.get(self.url)
