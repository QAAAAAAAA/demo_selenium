import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage


# Define a pytest fixture for WebDriver setup
@pytest.fixture(scope='function')
def driver():
   # Set up Chrome options for headless mode
   chrome_options = Options()
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('--disable-dev-shm-usage')


   # Define the path to the ChromeDriver executable
   chrome_driver_path = '/path/to/chromedriver'  # Update this path


   # Initialize WebDriver
   service = Service(executable_path=chrome_driver_path)
   driver = webdriver.Chrome(service=service, options=chrome_options)
   yield driver
   driver.quit()


# Define the test case with parameterized inputs
@pytest.mark.parametrize("username, password, expected_success", [
   ("valid_user", "valid_password", True),    # Valid credentials
   ("invalid_user", "valid_password", False),  # Invalid username
   ("valid_user", "invalid_password", False),  # Invalid password
   ("invalid_user", "invalid_password", False)  # Invalid username and password
])
def test_login(driver, username, password, expected_success):
   # Open the web application
   driver.get('https://practicetestautomation.com/practice-test-login')  # Update this URL


   # Create a LoginPage object
   login_page = LoginPage(driver)


   # Enter credentials and submit the form
   login_page.enter_username(username)
   login_page.enter_password(password)
   login_page.click_login_button()


   # Assert the login outcome based on expected success
   if expected_success:
       assert login_page.is_login_successful(username), "Login should be successful but was not."
   else:
       assert login_page.is_login_unsuccessful(), "Login should be unsuccessful but was not."
