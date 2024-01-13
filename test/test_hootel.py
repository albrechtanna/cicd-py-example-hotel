import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import pytest
import random



class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    @pytest.mark.parametrize("email, password", [('gebogip103@nexxterp.com', 'ghjk')])
    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")
    def test_login(self, email, password):
        menu_toggle = WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@class = 'navbar-toggler collapsed']")))
        menu_toggle.click()
        login_btn = WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable((By.XPATH, '//a[@class="nav-link"]')))
        login_btn.click()

        time.sleep(0.5)
        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys(email)

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys(password)

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()

        logout_btn = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable((By.ID, "logout-link")))

        assert logout_btn.text == "Kilépés"

    def test_hotel_list(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10

# házi feladat
    # TC1 - checkbox
    def test_hotel_checkbox(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        checkbox_list = self.browser.find_elements(By.XPATH, '//input[@type="checkbox"]')
        for checkbox in checkbox_list:
            checkbox.click()
            assert checkbox.is_selected()

    # TC2 - tetszőleges hotel oldal
    def test_hotel_page(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        first_hotel = self.browser.find_element(By.XPATH, '//h4[@style="cursor: pointer"]')
        first_hotel.click()
        time.sleep(1)

        back_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary"]')
        assert back_btn

    # TC3 - hosszú leírás
    def test_hotel_description(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_description = self.browser.find_elements(By.XPATH, '//p[@class="card-text"]')[1]
        print(hotel_description.text)

        assert hotel_description

    # TC4 - leiras hossza
    def test_hotel_desclength(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_description = self.browser.find_elements(By.XPATH, '//p[@class="card-text"]')[1]
        print(hotel_description.text)

        assert 500 <= len(hotel_description.text) <= 2000

    # TC5 - vissza
    def test_hotel_visszahotellista(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        first_hotel = self.browser.find_element(By.XPATH, '//h4[@style="cursor: pointer"]')
        first_hotel.click()
        time.sleep(1)

        back_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary"]')
        back_btn.click()
        time.sleep(5)

        first_hotel = self.browser.find_element(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert first_hotel
