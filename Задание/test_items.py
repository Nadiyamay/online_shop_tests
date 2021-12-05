import pytest
from selenium import webdriver
import time

def test_button_add_to_basket_checking(browser):

    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button=browser.find_elements_by_class_name("add-to-basket")
    time.sleep(7)
    assert button is not None
    