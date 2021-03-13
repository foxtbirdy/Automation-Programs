from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import re

user_name = input("Phone, email, username ? > ")
user_password = input("Password ? > ")

PATH = "D:\\Coding Nerds\\RFC\\edgedriver\\msedgedriver.exe"
driver = webdriver.Edge(PATH)

TWITTER_HOMEPAGE = "https://twitter.com/home"
driver.get(TWITTER_HOMEPAGE)
get_url = driver.current_url

def notify_info_error(user_name):
	print("The credentials of the username %s are not correct." % (user_name))
	time.sleep(2)
	print("Selenium will be quitting now.")
	time.sleep(3)
	driver.quit()

elem = WebDriverWait(driver , 20).until(
	expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label'))
)
elem.send_keys(user_name) 

elem_password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
elem_password.send_keys(user_password)

main = WebDriverWait(driver , 20).until(
	expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span'))
)
main.click()

REGEX_pattern = r"[@]"
modified_text = re.sub(REGEX_pattern , "" , user_name)

PASSWORD_REJECTED_1 = "https://twitter.com/login/error?username_or_email=%40"+modified_text+"&redirect_after_login=%2Fhome"
PASSWORD_REJECTED_2 = "https://twitter.com/login/error?username_or_email="+modified_text+"&redirect_after_login=%2Fhome"

currently = driver.current_url

if currently == PASSWORD_REJECTED_1:
	notify_info_error(user_name)
elif currently == PASSWORD_REJECTED_2:
	notify_info_error(user_name)

