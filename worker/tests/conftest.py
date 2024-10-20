import pytest

from selenium import webdriver
from unittest.mock import MagicMock

@pytest.fixture(scope='module')
def driver():
    return MagicMock()