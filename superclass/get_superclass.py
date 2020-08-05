import urllib.request
from bs4 import BeautifulSoup
import sys
import json

url = "https://en.wikipedia.org/wiki/Coronavirus_disease_2019"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")

cat_section = soup.find(id='mw-normal-catlinks')
super_categories = []

for cat in cat_section.findAll('a')[1:]:
    super_categories.append(cat.text)