import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'Кнопка добавления в корзину отсутствует'
    # time.sleep(30)