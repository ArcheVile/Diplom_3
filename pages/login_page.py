import allure
from .base_page import BasePage
from locators.auth_locators import AuthLocators

class LoginPage(BasePage):

    @allure.step("Открываем страницу логина")
    def open(self):
        super().open("/login")

    @allure.step("Переход по ссылке 'Забыли пароль'")
    def go_to_forgot_password(self):
        self.click_element(AuthLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Проверяем, что открыта страница логина")
    def is_login_page(self):
        return AuthLocators.LOGIN_BUTTON in self.driver.page_source
