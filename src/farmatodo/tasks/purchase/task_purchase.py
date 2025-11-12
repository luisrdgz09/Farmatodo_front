import logging

from src.farmatodo.Interactions.open_browser.go_login import GoLogin
from src.farmatodo.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess

logger = logging.getLogger(__name__)


class TaskPurchase:

    @staticmethod
    def add_purchase():
        logger.info("Adding purchase task executed.")
        # Aquí iría la lógica para agregar una compra
        driver = GoLogin.get_driver()
        # Ejemplo de interacción con la página para agregar una compra
        jacket_product = driver.locator("[data-test=\"item-5-title-link\"]")
        xpath_selector = '//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]'

        # Localiza el elemento usando el XPath
        price_locator = driver.locator(xpath_selector)

        UtilRememberDataProcess.set_price_product(price_locator.inner_text())
        UtilRememberDataProcess.set_name_product(jacket_product.inner_text())
        jacket_product.click()
        driver.locator("[data-test=\"add-to-cart\"]").click()
        driver.locator("[data-test=\"shopping-cart-link\"]").click()
        driver.locator("[data-test=\"item-5-title-link\"]").click()
        driver.locator("[data-test=\"shopping-cart-link\"]").click()

    @staticmethod
    def finish_purchase():
        driver = GoLogin.get_driver()
        driver.locator("[data-test=\"checkout\"]").click()
        driver.locator("[data-test=\"firstName\"]").click()
        driver.locator("[data-test=\"firstName\"]").fill("luis")
        driver.locator("[data-test=\"lastName\"]").click()
        driver.locator("[data-test=\"lastName\"]").fill("pruebas")
        driver.locator("[data-test=\"postalCode\"]").click()
        driver.locator("[data-test=\"postalCode\"]").fill("012056")
        driver.locator("[data-test=\"continue\"]").click()
        driver.locator("[data-test=\"finish\"]").click()
        driver.locator("[data-test=\"complete-header\"]").click()

