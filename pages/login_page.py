from .base_page import BasePage
from locators.auth_locators import AuthLocators

class LoginPage(BasePage):
    def open(self):
        super().open("/login")

    def go_to_forgot_password(self):
        self.click_element(AuthLocators.FORGOT_PASSWORD_LINK)

    def is_login_page(self):
        return AuthLocators.LOGIN_BUTTON in self.driver.page_source
