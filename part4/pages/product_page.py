from pages.base_page import BasePage  # type: ignore
from pages.locators import ProductPageLocators  # type: ignore


class ProductPage(BasePage):  # type: ignore
    def add_item_into_basket(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BTN
        ), "There ain't 'Add to basket' button"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def check_item_name_in_basket(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.ITEM_TITLE
        ), "There ain't item title"
        assert self.is_element_present(
            *ProductPageLocators.ITEM_TITLE_IN_BASKET
        ), "There ain't item title in basket"
        item_title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text
        basket_title = self.browser.find_element(
            *ProductPageLocators.ITEM_TITLE_IN_BASKET
        ).text
        assert item_title == basket_title, "There ain't item title in basket"

    def check_price_in_basket(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.ITEM_PRICE
        ), "There ain't item price"
        assert self.is_element_present(
            *ProductPageLocators.ITEM_PRICE_IN_BASKET
        ), "There ain't basket price"
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price in basket_price, "Basket price isn't equal to item price"

    def sucess_message_is_not_present(self) -> None:
        assert self.is_not_element_present(
            *ProductPageLocators.ADD_INTO_BASKET_SUCESS_MSG
        ), "Success message is presented, but should not be"

    def sucess_message_is_disappeared(self) -> None:
        assert self.is_disappeared(
            *ProductPageLocators.ADD_INTO_BASKET_SUCESS_MSG
        ), "Success message is disappeared, but should not be"
