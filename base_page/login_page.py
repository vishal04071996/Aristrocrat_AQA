import selenium

from selenium.webdriver.common.by import By


class login_page:
   enter_username = (By.XPATH,"//input[@placeholder='Username']")
   enter_password = (By.XPATH,"//input[@placeholder='Password']")
   click_login_button = (By.XPATH,"//input[@class='submit-button btn_action']")
   error_message = (By.XPATH,"//h3[@data-test='error']")


   def __init__(self, driver):
       self.driver = driver


   def login_username(self, username):
       self.driver.find_element(*self.enter_username).send_keys(username)


   def login_password(self, Password):
       self.driver.find_element(*self.enter_password).send_keys(Password)


   def login_click_login_button(self):
       self.driver.find_element(*self.click_login_button).click()


   def login_error_message(self):
       return self.driver.find_element(*self.error_message).text

