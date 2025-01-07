from selenium import webdriver
import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Test üçün konfiqurasiya
@pytest.fixture(scope="module")
def setup_driver():
    chrome_options = Options()
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test funksiyaları
def test_login_form_width(setup_driver):
    driver = setup_driver
    driver.get("https://userinyerface.com/game.html")
    element1 = driver.find_element(By.CLASS_NAME, 'login-form__field-row')
    assert element1.value_of_css_property("width") == "372px"

def test_login_form_height(setup_driver):
    driver = setup_driver
    element2 = driver.find_element(By.CLASS_NAME, 'login-form__field-row')
    assert element2.value_of_css_property("height") == "40px"

def test_email_field_width(setup_driver):
    driver = setup_driver
    element3 = driver.find_element(By.CLASS_NAME, 'align__cell')
    assert element3.value_of_css_property("width") == "133.688px"

def test_font_family(setup_driver):
    driver = setup_driver
    element4 = driver.find_element(By.CLASS_NAME, 'login-form__container')
    assert element4.value_of_css_property("font-family") == "sans-serif"
