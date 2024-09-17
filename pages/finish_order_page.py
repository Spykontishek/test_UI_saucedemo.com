import allure
from pages.base_page import BasePage
from locators.finish_order_page_locators import Locators_finish_order

class FinishOrderPage(BasePage):

    @allure.step('ожидание пока окно об успешном закаке станет видимым')
    def wait_order_success_to_be_visible(self):
        self.wait_element_to_be_visible_method(Locators_finish_order.BUY_SUCCESS)

    @allure.step('проверка, что окно об успешном закаке отображается')
    def Order_success_is_displayed(self):
        return self.element_is_displayed_method(Locators_finish_order.BUY_SUCCESS)