import allure
from .base_page import BasePage
from locators.auth_locators import AuthLocators

class ForgotPasswordPage(BasePage):

    @allure.step("Открываем страницу восстановления пароля")
    def open(self):
        super().open("/forgot-password")

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        email_input = self.find_element(AuthLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    @allure.step("Нажимаем кнопку 'Восстановить пароль'")
    def click_reset_button(self):
        self.click_element(AuthLocators.RESET_PASSWORD_BUTTON)

    @allure.step("Нажимаем на иконку отображения пароля")
    def click_show_password(self):
        self.click_element(AuthLocators.SHOW_PASSWORD_BUTTON)
        return self.find_element(AuthLocators.PASSWORD_INPUT).get_attribute("type")

