import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page.login_page import login_page
from utilites.read_properties import Read_Config


class Testsecnario2:
    wrong_username = Read_Config.get_wrong_username()
    password = Read_Config.get_Password()
    URL = Read_Config.get_URL()



    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.LP = login_page(self.driver)
        self.LP.login_username(self.wrong_username)
        self.LP.login_password(self.password)
        self.LP.login_click_login_button()
        text = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        print("Actual Error Message is:", text)
        print("Given Error Message is: Sorry, this user has been banned.")
        if "Sorry, this user has been banned." == text:
            print("Text Match")
        else:
            print("Text Mismatch")
        self.driver.get_screenshot_as_file("screenshot/screenshot_error.png")
        self.driver.quit()
