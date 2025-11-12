import logging
import os

from src.farmatodo.Interactions.open_browser.go_login import GoLogin
from src.farmatodo.models.login.page_login import PageLogin as p_login
logger = logging.getLogger(__name__)


class TaskLogin:

    @staticmethod
    def login_sauce_demo(user,password):
        GoLogin.open_login_responsive('Desktop Chrome')
        driver = GoLogin.get_driver()
        TaskLogin._write_user_and_password(driver, user, password)
        driver.locator(p_login.BTN_LOGIN).click()



    @staticmethod
    def _write_user_and_password(driver, user, password):
        driver.locator(p_login.TXT_USER).fill(user)
        driver.locator(p_login.TXT_PASSWORD).fill(password)


