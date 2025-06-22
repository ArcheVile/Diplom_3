from selenium.webdriver.common.by import By

class AuthLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
