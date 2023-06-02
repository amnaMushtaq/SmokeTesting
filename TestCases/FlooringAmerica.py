
from PageObject.CommonFiles import user_Login_to_siteadmin, close_the_browser, user_login_to_Yodle
from PageObject.FlooringAmericaPage import Navigate_to_Site, submit_form, validates_form_in_site_admin, \
    validates_form_in_centermark, get_Location_Information

# Run the test case
#TestCases
Navigate_to_Site("https://www.brunswickfloorsfa.com/")
submit_form()
user_Login_to_siteadmin()
validates_form_in_site_admin()
Location_Number,Location_Name=get_Location_Information()
user_login_to_Yodle()
validates_form_in_centermark(Location_Number,Location_Name)
close_the_browser()

# Close the browser















