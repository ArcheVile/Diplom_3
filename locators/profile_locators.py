from selenium.webdriver.common.by import By

class ProfileLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY = (By.XPATH, "//a[@href='/account/orders']")
    PROFILE_HEADER = (By.XPATH, "//h1[text()='Профиль']")
