#!/usr/bin/python3

import pandas as pd
import csv, time, random
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
browser.get("https://topcustomwritings.com/entrepreneurship-and-small-business-management-unit-9/")


df = pd.read_csv('homework.csv', index_col=0)

for i in range(-1,50):

        x  = i + 1

        #author_input
        author_input = browser.find_element_by_css_selector("input[id=author]")
        author_input.send_keys('name')
        time.sleep(0.5)

        #email_input
        email_input = browser.find_element_by_css_selector("input[id=email]")
        email_input.send_keys('datalock886@gmail.com')
        time.sleep(0.5)

        #comment_input
        comment_input = browser.find_element_by_css_selector("textarea[id=comment]")
        comment_input.send_keys(df.iloc[x])
        time.sleep(0.5)

        send_comment_button = browser.find_element_by_id("submit")
        send_comment_button.click()
        time.sleep(2)
        browser.refresh()
