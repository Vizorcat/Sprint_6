import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.suite("Logo Tests")
@allure.title("Проверка перехода по логотипу Самоката")
@allure.description("Тест проверяет, что при нажатии на логотип Самоката пользователь возвращается на главную страницу.")
@allure.severity(allure.severity_level.NORMAL)
def test_scooter_logo_redirect(driver):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(driver)
    with allure.step("Нажатие на логотип Самоката"):
        main_page.click_scooter_logo()
    with allure.step("Проверка, что URL соответствует главной странице"):
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Логотип Самоката не ведет на главную страницу"

@allure.title("Проверка перехода по логотипу Яндекса")
@allure.description("Тест проверяет, что при нажатии на логотип Яндекса открывается главная страница Дзена в новой вкладке.")
@allure.severity(allure.severity_level.NORMAL)
def test_yandex_logo_redirect(driver):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(driver)
    with allure.step("Нажатие на логотип Яндекса"):
        main_page.click_yandex_logo()
    with allure.step("Ожидание новой вкладки и переключение на неё"):
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
    with allure.step("Проверка, что URL содержит dzen.ru"):
        WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url)
        assert "dzen.ru" in driver.current_url, "Логотип Яндекса не ведет на главную страницу Дзена"