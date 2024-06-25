###Test case ID: TC_PIM_03

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

##locating the Forgot your Password element
forgot_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]')))
forgot_link.click()

# entering the username for password reset
username = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')))
username.send_keys('Admin')

driver.maximize_window()

# Locating the Reset password button
reset_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
reset_button.click()
time.sleep(5)
driver.close()