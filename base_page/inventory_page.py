import selenium

from selenium.webdriver.common.by import By


class inventory_page:
   enter_username = (By.XPATH,"//input[@placeholder='Username']")
   enter_password = (By.XPATH,"//input[@placeholder='Password']")
   login_button_locator = (By.XPATH,"//input[@class='submit-button btn_action']")
   logout_tab = (By.XPATH, "//button[@id = 'react-burger-menu-btn']")
   logout_button = (By.XPATH,"//a[@id = 'logout_sidebar_link']")
   login_button_check = (By.XPATH,"//input[@type='submit']")


   def __init__(self, driver):
       self.driver = driver


   def login_username(self, username):
       self.driver.find_element(*self.enter_username).send_keys(username)


   def login_password(self, Password):
       self.driver.find_element(*self.enter_password).send_keys(Password)


   def click_login_button(self):
       self.driver.find_element(*self.login_button_locator).click()

   def click_menu_tab(self):
       return self.driver.find_element(*self.logout_tab).click()

   def click_logout_button(self):
       self.driver.find_element(*self.logout_button).click()

   def get_login_button_class(self):
       return self.driver.find_element(*self.login_button_check).get_attribute("class")




