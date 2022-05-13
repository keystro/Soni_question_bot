#!/usr/bin/python3

import requests, lxml
from bs4 import BeautifulSoup

url = 'https://www.transtutors.com/questions/humanities'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
footer_element = soup.select_one('a.current')
print(footer_element.text.strip())