from .base_page import BasePage
from locators.auth_locators import AuthLocators


class ForgotPasswordPage(BasePage):
    def go_to_forgot_password(self):
        self.click_element(AuthLocators.FORGOT_PASSWORD_LINK)

    def enter_email(self, email):
        email_field = self.find_element(AuthLocators.EMAIL_INPUT)
        email_field.send_keys(email)

    def click_reset_button(self):
        self.click_element(AuthLocators.RESET_PASSWORD_BUTTON)

    def click_show_password(self):
        self.click_element(AuthLocators.SHOW_PASSWORD_BUTTON)
        return self.find_element(AuthLocators.PASSWORD_INPUT).get_attribute("type")