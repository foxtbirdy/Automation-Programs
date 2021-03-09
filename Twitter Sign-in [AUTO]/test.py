from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


user_name = input("Phone, email, username ? > ")
user_password = input("Password ? > ")

PATH = "Change me!"
driver = webdriver.Edge(PATH)
driver.get("http://www.twitter.com/login")

time.sleep(3)

elem_username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label')
elem_username.send_keys(user_name) 
time.sleep(3)
elem_password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
elem_password.send_keys(user_password)

time.sleep(3)

elem_clicker = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span')
elem_clicker.click()
