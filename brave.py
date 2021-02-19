# Brave Browser Follow/Unfollow
from idlelib import browser
import password as password
from selenium import webdriver
from time import sleep

driver_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/chromedriver.exe" # Change driver path.
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # Change brave path.
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=driver_path, options=option)

def Follow():
    browser.get("https://www.instagram.com")
    sleep(5)
    browser.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')\
        .click()
    browser.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(" ") # Input your email here.
    browser.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(" ") # Input your password here.
    browser.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    sleep(5)
    browser.get("https://www.instagram.com/explore/people/suggested/")
    sleep(5)
    while True:
        for f in range(10):
            browser.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]') \
                .click()
        sleep(3)
        browser.refresh()
        sleep(3)
    
def Unfollow():
    browser.get("https://www.instagram.com")
    sleep(5)
    browser.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')\
        .click()
    browser.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(" ") # Input your email here.
    browser.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(" ") # Input your password here.
    browser.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    sleep(5)
    browser.get("https://www.instagram.com/quercusub/")
    following = browser.find_element_by_partial_link_text("following")
    following.click()
    sleep(5)
    while True:
        for i in range(10):
            browser.find_element_by_xpath('//button[text()="Following"]')\
                .click()
            sleep(1)
            browser.find_element_by_xpath('//button[text()="Unfollow"]')\
                .click()
            sleep(1)
        browser.refresh()
        sleep(3)
        following = browser.find_element_by_partial_link_text("following")
        following.click()
        sleep(3)

# To use any of these functions, uncomment one of them.
#Follow()
#Unfollow()
