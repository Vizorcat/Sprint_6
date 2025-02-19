import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service()

    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru")
    yield driver
    driver.quit()