import allure
from locators.second_order_page_locators import Locators_order_2
from pages.base_page import BasePage

class SecondOrderPage(BasePage):
    @allure.step('Клик по кнопке "Finish')
    def click_finish_button(self):
        self.click_method(Locators_order_2.FINISH_BUTTON)
