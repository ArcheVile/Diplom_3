from selenium.webdriver.common.by import By

class MainLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")
    INGREDIENT = (By.XPATH, "//div[@class='BurgerIngredient_ingredient__1TVf6']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter')]")
    INGREDIENT_MODAL = (By.XPATH, "//div[@class='Modal_modal__P3_V8']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'modal_close')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_SUCCESS = (By.XPATH, "//h2[text()='Ваш заказ начали готовить']")
