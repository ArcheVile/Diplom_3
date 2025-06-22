import pytest
import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.go_to_forgot_password()
        assert "forgot-password" in driver.current_url

    @allure.title("Ввод почты и восстановление пароля")
    def test_reset_password(self, driver, test_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open()
        forgot_page.enter_email(test_user["email"])
        forgot_page.click_reset_button()
        assert "reset" in driver.current_url

    @allure.title("Показать/скрыть пароль")
    def test_show_hide_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open()
        input_type = forgot_page.click_show_password()
        assert input_type == "text"
