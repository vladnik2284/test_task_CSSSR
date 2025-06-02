from selene import browser, be, have
from the_constant import *

def test_fill_form():
    browser.element(UNDER_THE_HEADING).should(be.visible) # Проверяем что данный элемнт виден.
    browser.element(UNDER_THE_HEADING).should(have.css_property('font-weight', '400')) # Проверяет элемент на наличие свойств font-weight = 400

