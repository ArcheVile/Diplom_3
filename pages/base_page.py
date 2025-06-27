import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"

    @allure.step("Открываем страницу: {path}")
    def open(self, path=""):
        self.driver.get(self.base_url + path)

    @allure.step("Находим элемент: {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Кликаем по элементу: {locator}")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получаем текст элемента: {locator}")
    def get_element_text(self, locator):
        return self.find_element(locator).text
