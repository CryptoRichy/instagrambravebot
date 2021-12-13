# Instagram Brave Bot
# Made for Linux. Created by https://github.com/Splintaz

import password as password
from selenium import webdriver
from time import sleep
import argparse
import textwrap

def Follow(parsed_args):
    chromedriverpath = "/usr/bin/chromedriver"
    bravepath = "/opt/brave.com/brave/brave"
    ig_username = input("Instagram username: ")
    ig_password = input("Instagram password: ")
    chromedriver_path = str(chromedriverpath) 
    brave_path = str(bravepath) 
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=option)
    browser.get("https://www.instagram.com")
    sleep(5)
    browser.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')\
        .click()
    browser.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(ig_username) 
    browser.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(ig_password)
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
    
def Unfollow(parsed_args):
    chromedriverpath = input("Chromedriver path: ")
    bravepath = input("Brave path: ")
    ig_username = input("Instagram username: ")
    ig_password = input("Instagram password: ")
    chromedriver_path = str(chromedriverpath) 
    brave_path = str(bravepath) 
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=option)
    browser.get("https://www.instagram.com")
    sleep(5)
    browser.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')\
        .click()
    browser.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(ig_username)
    browser.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(ig_password)
    browser.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    sleep(5)
    browser.get("https://www.instagram.com/"+ig_username) 
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

parser = argparse.ArgumentParser(description="This is a Instagram unfollow/follow bot which uses Selenium to automate its functions, with the Brave Browser.", epilog=textwrap.dedent("Created by https://github.com/Splintaz"))
parser.add_argument('--follow', dest='action', action='store_const', const=Follow)
parser.add_argument('--unfollow', dest='action', action='store_const', const=Unfollow)
parsed_args = parser.parse_args()
if parsed_args.action is None:
    parser.parse_args(['-h'])
parsed_args.action(parsed_args)
