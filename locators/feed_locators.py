from selenium.webdriver.common.by import By

class FeedLocators:
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V8')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'modal_close')]")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
