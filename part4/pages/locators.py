from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_FORGOT_PASSWORD = (By.CSS_SELECTOR, "#login_form > p > a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form button")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    LOGIN_FORM_FULL = (
        LOGIN_FORM,
        LOGIN_USERNAME,
        LOGIN_PASSWORD,
        LOGIN_FORGOT_PASSWORD,
        LOGIN_BUTTON,
    )
    REGISTRATION_FORM_FULL = (
        REGISTRATION_FORM,
        REGISTRATION_EMAIL,
        REGISTRATION_PASSWORD,
        REGISTRATION_CONFIRM_PASSWORD,
        REGISTRATION_BUTTON,
    )


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ITEM_TITLE = (
        By.CSS_SELECTOR,
        "#content_inner > article > div.row > div.col-sm-6.product_main > h1",
    )
    ITEM_PRICE = (By.CSS_SELECTOR, "div.row .price_color")
    ITEM_TITLE_IN_BASKET = (
        By.CSS_SELECTOR,
        "#messages > div:nth-child(1) > div > strong",
    )
    ITEM_PRICE_IN_BASKET = (By.CSS_SELECTOR, "header div.basket-mini")
    ADD_INTO_BASKET_SUCESS_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasketPageLocators:
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
