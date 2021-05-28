from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Type your username and passwords
usernameStr = 'username'
passwordStr = 'pass'

# Write path of chromedriver.exe in your computer
browser = webdriver.Chrome('chromedriver.exe_path')
browser.get(('https://stackoverflow.com/'))

loginBtn = browser.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')
loginBtn.click()

username = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/form/div[1]/div/input')
username.send_keys(usernameStr)

password = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/form/div[2]/div[1]/input')
password.send_keys(passwordStr)

login=browser.find_element_by_xpath('//*[@id="submit-button"]')
login.click()

