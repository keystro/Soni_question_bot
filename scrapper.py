#!/usr/bin/python3

#imports
import time, csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome('./chromedriver')

questions = []


print("This program will take a while to execute, so we suggest making a cup of coffee while you wait")
for x in range(-1, 200):
    x += 1
    url = 'https://www.transtutors.com/questions/accounting/%d' %(x)
    driver.get(url)
    print(f"page {x}: ")

    Qfile = {'Page Num': x, 'Questions': questions}
    for i in range(0, 50):
        i += 1
        link = driver.find_element(By.XPATH, "/html/body/form/section/section[2]/div/div/div/div/div[2]/div/div/ul/li[%d]/a/div/div[2]/h3" %(i))
        questions.append(link.text)
    
    print(len(questions))
   
    df = pd.DataFrame(Qfile)
    with open('homework.csv' ,'a') as f:
        df.to_csv(f, header=f.tell()==0, index=True)

    driver.delete_all_cookies()
    time.sleep(3)