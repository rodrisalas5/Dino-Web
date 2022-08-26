from src.pages.Python.dino_web import DinoWebPage
import pytest


def test_menu_is_display(browser):
    home_page = DinoWebPage(browser)
