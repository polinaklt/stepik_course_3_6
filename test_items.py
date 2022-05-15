from selenium.webdriver.common.by import By
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_displayed(browser):
    browser.get(LINK)
    assert browser.find_element(
        By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed(), \
        "There is no 'Add to basket' button"

