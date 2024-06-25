##Test case ID: TC_PIM_02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

# Setup Automatic WebDriver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Setup WebDriver path and options
# paths = r"D:\ProgramS\PyCharm\chromedriver.exe"
# os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# Getting the Webpage inputs
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

##locating the username & password element and passing values
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
username.send_keys('Admin')

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
password.send_keys('admin123')

driver.maximize_window()

## Clicking the login button to enter
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()

# verifying the present element is holding "OrangeHRM" as title page
WebDriverWait(driver,300).until(EC.title_contains("OrangeHRM"))
print(driver.title)

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/head/title")))

print(element.get_attribute("innerHTML"))

# Locating the Options on the Admin Page
main_menu= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")))
main_menu.click()
time.sleep(5)
driver.close()