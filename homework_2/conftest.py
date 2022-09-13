import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def window_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
