import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(autouse=True)
def set_browser_size():
    browser.config.window_width = 480
    browser.config.window_height = 720


def test_positive_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('OfhhriUJHFsgr547udSYGDqwtsg94jJcnefsakZbdfkjlUH').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
