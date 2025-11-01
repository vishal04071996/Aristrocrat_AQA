import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page.login_page import login_page
from utilites.read_properties import Read_Config

class Testsecnario1:
    username = Read_Config.get_username()
    password = Read_Config.get_Password()
    URL = Read_Config.get_URL()

    @pytest.mark.smoke
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.URL)

        self.LP = login_page(self.driver)
        self.LP.login_username(self.username)
        self.LP.login_password(self.password)
        self.LP.login_click_login_button()
        assert "Swag Labs" in self.driver.title
        self.driver.get_screenshot_as_file("screenshot/screenshot_login.png")
        self.driver.quit()
