from selenium.webdriver.common.by import By


class Locators_cart:
    ANY_PRODUCT = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    CHECKOUT_BUTTON = (By.ID, "checkout")