from selenium.webdriver.common.by import By


class Locators_prod_list:
    ANY_PRODUCT = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")