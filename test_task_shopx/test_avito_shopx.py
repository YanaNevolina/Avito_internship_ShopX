import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAvitoShopX:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_buy_with_delivery_phone_is_empty(self):
        self.login("REPLACE:login", "REPLACE:password")
        self.go_to_home()

        self.select_category_personal()
        self.select_with_delivery()
        self.show_results()

        self.click_list_item()
        self.select_tab(1)

        self.click_buy_with_delivery()

        self.check_phone_is_empty()

    def check_phone_is_empty(self):
        value = self.driver.find_element(By.NAME, "phone").get_attribute("value")
        assert value == ""

    def click_buy_with_delivery(self):
        self.driver.find_element(By.CSS_SELECTOR, ".item-buyer-button-1-zak").click()

    def show_results(self):
        self.driver.find_element(By.XPATH, "//div[2]/button").click()

    def select_with_delivery(self):
        self.driver.find_element(By.XPATH, "//div[5]/div/div/div/div/div/div/label/span").click()

    def select_tab(self, tab_number: int):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def click_list_item(self):
        self.driver.find_element(By.XPATH, "//a[contains(concat(\' \',normalize-space(@data-marker),\' \'),\' item-title\')]").click()

    def select_category_personal(self):
        self.driver.find_element(By.ID, "category").click()
        dropdown = self.driver.find_element(By.ID, "category")
        dropdown.find_element(By.XPATH, "//option[. = 'Личные вещи']").click()

    def go_to_home(self):
        self.driver.get("https://www.avito.ru/sochi")

    def login(self, login: str, password: str):
        self.driver.get("https://www.avito.ru/")
        self.driver.find_element(By.LINK_TEXT, "Вход и регистрация").click()
        self.driver.find_element(By.NAME, "login").send_keys(login)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "submit").click()
