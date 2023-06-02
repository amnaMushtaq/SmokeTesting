import sys
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.FlooringAmericaPage import Navigate_to_Site, submit_form, validate_form_in_site_admin, \
    get_Location_Information, validate_form_in_centermark

# ser = Service("C:\drivers\chromedriver.exe")
# # Create a new instance of the Chrome driver
# driver=webdriver.Chrome(service=ser)
# # Function to submit the form on the contact us page
# def Navigate_to_Site(url):
#     try:
#         driver.get(url)
#         driver.maximize_window()
#         print(driver.title)
#         Current_Url=driver.current_url
#         print(Current_Url)
#         if Current_Url==url:
#             print("URL is correct")
#         else:
#             print("URL is redirecting")
#
#
#         driver.find_element(By.LINK_TEXT,"Contact Us").click()
#     except WebDriverException as e:
#         if "ERR_CONNECTION_TIMED_OUT" in str(e):
#             print("Connection timed out. Please check your internet connection or the website URL.")
#         else:
#             print("An unexpected WebDriverException occurred:", str(e))
#
#
# def submit_form():
#     try:
#         driver.find_element(By.NAME,"FirstName").send_keys("Test Lead")
#         driver.find_element(By.NAME,"LastName").send_keys("CCA Please Ignore")
#         driver.find_element(By.NAME,"CleanHomePhone").send_keys("9056428161")
#         driver.find_element(By.NAME,"PostalCode").send_keys("99501")
#         driver.find_element(By.NAME,"EmailAddress").send_keys("testleadfa06012023@ccapleaseignore.com")
#         driver.find_element(By.NAME,"OpportunityNotes").send_keys("Test Lead")
#         #driver.find_element(By.name,"MainFormCheckBox").get_attribute("checked")
#         driver.find_element(By.ID,"contact").click()
#         #driver.implicitly_wait(10)
#         #wait=WebDriverWait(driver,10)
#         #element=wait.until(EC.visibility_of_element_located(By.ID,"primary"))
#         time.sleep(5)
#         #CSS selector
#         #message=driver.find_element(By.CSS_SELECTOR,"section[role='main'] h2").text
#         message=driver.find_element(By.XPATH,"//section[@role='main']//h2").text
#         print(message)
#         assert "THANK YOU" in message
#         # #driver.close()
#     except KeyboardInterrupt:
#         print("Program interrupted by user.")
#         sys.exit()
#
# # Function to login to the site admin and validate the submitted form through email
# def validate_form_in_site_admin():
#
#     #UserLogin to the SiteAdmin
#     driver.find_element(By.XPATH, "//a[@href='/siteadmin/home']").click()
#     window_handles=driver.window_handles
#     driver.switch_to.window(window_handles[1])
#     driver.find_element(By.ID,"Email").send_keys("amna.mushtaq@enspireforenterprise.com")
#     driver.find_element(By.ID,"Password").send_keys("All@h!$1INDEED")
#     driver.find_element(By.XPATH,"//input[@type='submit']").click()
#     driver.find_element(By.XPATH,"//text()[contains(., 'Customer Management')]/following-sibling::a[contains(., 'Edit Now')]").click()
#     driver.find_element(By.ID,"users").click()
#     driver.find_element(By.XPATH,"//*[@id='users']/option[2]").click()
#     driver.find_element(By.ID,"cashGo").click()
#     driver.find_element(By.ID,"btnAllProjectsOpportunities").click()
#     # time.sleep(5)
#     # page_content=driver.page_source
#     # print(page_content)
#     # assert "testleadfa05302023@ccapleaseignore.com" in page_content
#     rows=driver.find_elements(By.XPATH,"//*[@id='json_data']/tr/td[6]")
#     for row in rows:
#         row_content=row.text
#         if "testleadfa06012023@ccapleaseignore.com" in row_content:
#             print("Element found in CASH", row_content)
#             break
#
#         else:
#             raise AssertionError("Element not found")
#
#     print("finish")
#     #Get Location Number
#     driver.find_element(By.ID,"back").click()
#     driver.find_element(By.ID,"back").click()
#
#     driver.find_element(By.XPATH,"//a[@href='/siteadmin/home']").click()
#
# # LocationNumber=None
# # LocationName=None
#
# def get_Location_Information():
#     #GetLocationNumber
#     driver.find_element(By.XPATH,"//text()[contains(., 'Enterprise Data')]/following-sibling::a[contains(., 'Edit Now')]").click()
#     LocationNumber=driver.find_element(By.NAME,"locationnumber").text
#     LocationName=driver.find_element(By.NAME,"clubname").text
#
#     print(LocationNumber)
#     print(LocationName)
#     return LocationNumber,LocationName
#
#
# # Function to login to Centermark and validate the submitted form through email
# def validate_form_in_centermark(LocNumber,LocName):
# #Centermark
#
#     driver.get("http://live.yodle.com/")
#     driver.find_element(By.ID,"usernameForm").send_keys("amna.mushtaq@enspireforenterprise.com")
#     driver.find_element(By.ID,"password").send_keys("Alhumdul!ll@h#1122")
#     driver.find_element(By.NAME,"submit").click()
#     SearchBox=driver.find_element(By.ID,"filterText")
#     SearchBox.send_keys(LocNumber)
#     SearchBox.send_keys(Keys.ENTER)
#     driver.find_element(By.XPATH,f"//*[text()='{LocName}']").click()
#
#     RecentEmails=driver.find_elements(By.XPATH,"//table[@id='contacts']/tbody/tr/td[3]")
#     for email in RecentEmails:
#         RecentEmail=email.text
#         print(RecentEmail)
#         if "testleadfa06012023@ccapleaseignore.com" in RecentEmail:
#             print("Email Found in Yodle", RecentEmail)
#             break

# Run the test case
#TestCases
Navigate_to_Site("https://www.brunswickfloorsfa.com/")
submit_form()
validate_form_in_site_admin()
Location_Number,Location_Name=get_Location_Information()
validate_form_in_centermark(Location_Number,Location_Name)

# Close the browser















