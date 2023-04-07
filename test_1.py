from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)


def test_result(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_no_result(browser_open):
    browser.element('[name="q"]').should(be.blank).type('ertfghvbnmjhvby4%$vfx crf hgfc').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Проверка #1 = 1 результат; Проверка #2 = 0 результатов')