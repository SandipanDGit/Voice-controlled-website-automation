import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(executable_path='F:\my software\geckodriver\geckodriver-v0.26.0-win64\geckodriver.exe')

def login():
    browser.get('https://lichess.org/login?referrer=/')
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')

    username.send_keys('nemesis_bot')
    password.send_keys('11031997')
    password.send_keys(Keys.ENTER)

# WebDriverWait(browser, 200)
# time.sleep(5)

def create_game(command):
    time.sleep(5)
    if command == '1+0':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[1]/div[1]')
        elem.click()
    elif command == '2+1':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[2]/div[1]')
        elem.click()
    elif command == '3+0':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[3]/div[1]')
        elem.click()
    elif command == '3+2':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]')
        elem.click()
    elif command == '5+0':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[5]/div[1]')
        elem.click()
    elif command == '5+3':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[6]/div[1]')
        elem.click()
    elif command == '10+0':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[7]/div[1]')
        elem.click()
    elif command == '10+5':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[8]/div[1]')
        elem.click()
    elif command == '15+10':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[9]/div[1]')
        elem.click()
    elif command == '30+0':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[10]/div[1]')
        elem.click()
    elif command == '30+20':
        elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[11]/div[1]')
        elem.click()
    elif command == 'custom':
        # elem = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[12]/div[1]')
        # elem.click()
        print('currently unavailable')
    else:
        print('invalid command')

def make_move(move):
    move_slot = browser.find_element_by_class_name('ready')
    move_slot.send_keys(Keys.CONTROL + "a")
    move_slot.send_keys(Keys.DELETE)
    move_slot.send_keys(move)
    time.sleep(2)
    
