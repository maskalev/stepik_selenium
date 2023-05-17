from pages.base_page import BasePage  # type: ignore
from pages.locators import BasketPageLocators  # type: ignore


class BasketPage(BasePage):  # type: ignore
    def is_empty_basket(self) -> None:
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Basket isn't empty, but should be"

    def is_empty_basket_message(self) -> None:
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MSG
        ), "There ain't 'empty basket' message"
