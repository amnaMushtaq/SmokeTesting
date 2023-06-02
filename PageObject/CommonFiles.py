from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



ser = Service("C:\drivers\chromedriver.exe")
# Create a new instance of the Chrome driver
global driver
driver=webdriver.Chrome(service=ser)

def user_Login_to_siteadmin():
    driver.find_element(By.XPATH, "//a[@href='/siteadmin/home']").click()
    window_handles=driver.window_handles
    driver.switch_to.window(window_handles[1])
    driver.find_element(By.ID,"Email").send_keys("amna.mushtaq@enspireforenterprise.com")
    driver.find_element(By.ID,"Password").send_keys("All@h!$1INDEED")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()