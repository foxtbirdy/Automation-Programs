from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import re


# The first step is to give the username and the password.
user_name = input("Phone, email, username ? > ")
user_password = input("Password ? > ")
 
################################                        ################################ 
################################ CHANGE THE CODE BELOW! ################################
################################			################################ 


# I am using Windows so my driver application is a .exe file located at this directory.
# I added a reference link to show you how to link your webdriver with python selenium program.
PATH = "D:\\Coding Nerds\\RFC\\edgedriver\\msedgedriver.exe"
driver = webdriver.Edge(PATH)

################################                        ################################ 
################################ CHANGE THE CODE ABOVE! ################################
################################			################################ 


#Main target is the twitter home. Since it will spawn a new browser window, the twitter servers will redirect us to the /login page.
TWITTER_HOMEPAGE = "https://twitter.com/home"
driver.get(TWITTER_HOMEPAGE)

# Use the current.url to get the current url address that the selenium is navigatiing on. 
get_url = driver.current_url

# Just a small program that notifies you IF your credentials are not correct.
def notify_info_error(user_name):
	print("The credentials of the username %s are not correct." % (user_name))
	time.sleep(2)
	print("Selenium will be quitting now.")
	time.sleep(3)
	driver.quit()

# Using the expected conditions allows us to locate the elements faster rather than using a time.sleep(number). Simply the elem uses the WebDriverWait to hold the selenium browser for a amount of time before it locates the expected elemets. The XPATH or element path is for the username.
elem = WebDriverWait(driver , 20).until(
	expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label'))
)
elem.send_keys(user_name) 

# The XPATH of the elem_password is for the password form fillup.
elem_password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
elem_password.send_keys(user_password)

# After the whole two forms are completed, the program will click the "Login" button that is located via another XPATH.
main = WebDriverWait(driver , 20).until(
	expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span'))
)
main.click()



#############                #############
############# EXPECTION ZONE #############
#############                #############

# this Regex Pattern removes the @ if it was added.
REGEX_pattern = r"[@]"
modified_text = re.sub(REGEX_pattern , "" , user_name)

# This value is when a user types @
PASSWORD_REJECTED_1 = "https://twitter.com/login/error?username_or_email=%40"+modified_text+"&redirect_after_login=%2Fhome"
# This value is when a user doesn't type @
PASSWORD_REJECTED_2 = "https://twitter.com/login/error?username_or_email="+modified_text+"&redirect_after_login=%2Fhome"

# if the credentials are incorrect, The website will redirect to anyone of this links. If none is triggered, that means that the program has successfully passed the /login url.
if get_url == PASSWORD_REJECTED_1:
	notify_info_error(user_name)
elif get_url == PASSWORD_REJECTED_2:
	notify_info_error(user_name)

