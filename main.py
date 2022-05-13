#!/usr/bin/python3

import requests, csv
import pandas as pd
from bs4 import BeautifulSoup
  
  
#for i in range(0,200):
url = requests.get("https://www.transtutors.com/questions/accounting/")
soup = BeautifulSoup(url.content, 'html.parser')

questions = []
Qfile = {'Questions': questions}

for n in soup.select('h3'):
    questions.append(n.text)

print(len(questions))

df = pd.DataFrame(Qfile)
with open('homework.csv' ,'a') as f:
    df.to_csv(f, header=f.tell()==0, index=True)

#file = open("homework.csv")
#reader = csv.reader(file)
#print (len(list(reader)))

