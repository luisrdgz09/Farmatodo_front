from playwright.sync_api import expect

from src.farmatodo.Interactions.open_browser.go_login import GoLogin
from src.farmatodo.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess


class QuestionPurchase:


    @staticmethod
    def validate_details_product():
        driver = GoLogin.get_driver()
        name_product =UtilRememberDataProcess.get_name_product()
        price_product =UtilRememberDataProcess.get_price_product()
        expect(driver.locator("[data-test=\"inventory-item-name\"]")).to_contain_text(f"{name_product}")
        expect(driver.locator("[data-test=\"inventory-item-price\"]")).to_contain_text(f"{price_product}")
    @staticmethod
    def validate_successful_purchase():
        driver = GoLogin.get_driver()
        expect(driver.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")





