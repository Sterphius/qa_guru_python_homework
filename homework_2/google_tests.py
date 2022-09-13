from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene github').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_should_find_nothing():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type("zmmzmmasdmfmafdsf").press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
