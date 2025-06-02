import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.window_height = 1080 # Определяем высоту браузера.
    browser.config.window_width = 1920 #Определяем ширину браузера
    driver_options = webdriver.ChromeOptions() # Создаёт новый экземпляр класса, для настройки браузера
    driver_options.page_load_strategy = 'eager' # Определяем как будет загружаться браузер, в данном случае не будет ждать загрузок картинок
    browser.config.driver_options = driver_options # Устанавливаем набор настроек созданных нами вебдрайверу
    browser.open('https://csssr.github.io/qa-engineer/') # Открываем данную страницу перед запуском тестов.

