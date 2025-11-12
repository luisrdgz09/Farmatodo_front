import logging

import playwright
from playwright.sync_api import sync_playwright

from src.farmatodo.conf.browser.conf_browser import ConfBrowser

logger = logging.getLogger(__name__)


class GoLogin:
    _playwright = None
    _browser_driver = None
    _driver = None

    @staticmethod
    def start_playwright():
        if GoLogin._playwright is None:
            GoLogin._playwright = sync_playwright().start()
        return GoLogin._playwright

    @staticmethod
    def stop_playwright():
        if GoLogin._browser_driver:
            GoLogin._browser_driver.close()
        if GoLogin._playwright:
            GoLogin._playwright.stop()
            GoLogin._playwright = None



    @staticmethod
    def get_driver():
        if GoLogin._driver is None:
            raise RuntimeError("El navegador no esta disponible.")
        return GoLogin._driver

    @staticmethod
    def open_login_responsive(dispositive):
        if GoLogin._playwright is None:
            GoLogin.start_playwright()
        dispositive_responsive = GoLogin._playwright.devices[dispositive]
        url = ConfBrowser.get_url()
        GoLogin._browser_driver = GoLogin._playwright.chromium.launch(
            headless=False, args=["--start-maximized"]
        )
        context = GoLogin._browser_driver.new_context(
            **dispositive_responsive,
        )
        GoLogin._driver = context.new_page()
        GoLogin._driver.goto(url)