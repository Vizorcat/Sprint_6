import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.suite("Order Flow Tests")
@pytest.mark.parametrize("button_type", ["top", "bottom"])
@pytest.mark.parametrize("order_data", [
    {"name": "Иван", "lastname": "Иванов", "address": "Москва, ул. Ленина, 1", "metro_station": "Белорусская", "phone": "+79000000000"},
    {"name": "Мария", "lastname": "Петрова", "address": "Санкт-Петербург, ул. Пушкина, 2", "metro_station": "Сенная площадь", "phone": "+79111111111"}
])
@allure.title("Проверка процесса заказа самоката через кнопку: {button_type}")
@allure.description("Тест проверяет полный процесс оформления заказа через верхнюю или нижнюю кнопку.")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_flow(driver, button_type, order_data):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(driver)

    with allure.step(f"Нажатие на кнопку заказа: {button_type}"):
        if button_type == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

    with allure.step("Заполнение формы заказа"):
        order_page = OrderPage(driver)
        order_page.fill_order_form(
            name=order_data["name"],
            lastname=order_data["lastname"],
            address=order_data["address"],
            metro_station=order_data["metro_station"],
            phone=order_data["phone"]
        )
        order_page.click_next_button()

    with allure.step("Переход на следующую страницу"):
        success_message = order_page.get_success_message()
        assert "Про аренду" in success_message, "Нет перехода на страницу Про аренду"