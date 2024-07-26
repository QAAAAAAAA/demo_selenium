from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)


   def enter_username(self, username):
       username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
       username_field.clear()
       username_field.send_keys(username)


   def enter_password(self, password):
       password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
       password_field.clear()
       password_field.send_keys(password)


   def click_login_button(self):
       submit_button = self.wait.until(EC.element_to_be_clickable((By.NAME, 'submit')))
       submit_button.click()


   def is_login_successful(self, username):
       # Adjust the condition based on what indicates a successful login
       return username in self.driver.page


   def is_login_unsuccessful(self):
       # Adjust the condition based on what indicates a failed login
       # For example, if there's an error message:
       try:
           error_message = self.wait.until(EC.visibility_of_element_located((By.ID, 'error_message')))
           return error_message.is_displayed()
       except:
           return False
