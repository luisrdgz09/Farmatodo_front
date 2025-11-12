import os

import allure
import pytest

from src.farmatodo.exceptions.purchase.question_purchase import QuestionPurchase
from src.farmatodo.tasks.purchase.task_purchase import TaskPurchase
from src.farmatodo.tasks.login.task_login import TaskLogin


@pytest.mark.e1_successful_purchase
@pytest.mark.purchase
@pytest.mark.run(order=1)
@allure.feature('Realizar compra')
def test_successful_purchase():
    with allure.step("Inicio de sesión exitoso"):
        task_login = TaskLogin()
        task_login.login_sauce_demo('standard_user','secret_sauce')
    with allure.step("Agregar producto"):
        exceptions_login = QuestionPurchase()
        task_purchase = TaskPurchase()
        task_purchase.add_purchase()
    with allure.step("fvalidar detalles del producto agregado y finalizar compra"):
        exceptions_login.validate_details_product()
        task_purchase.finish_purchase()
        exceptions_login.validate_successful_purchase()



