import urllib.request
from bs4 import BeautifulSoup
import sys
import json

url = sys.argv[1]
# url = https://en.wikipedia.org/wiki/Glossary_of_calculus
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")


terms = soup.findAll('dt', class_='glossary')
definitions = soup.findAll('dd', class_='glossary')

assert(len(terms) == len(definitions))

final_list = []

for i in range(len(terms)):

    obj = {
        "standard" : {
            'term': terms[i].text,
            'definition': definitions[i].text
            },
        "system": {
            'term': '',
            'definition': ''
            }
    }

    final_list.append(obj)

with open('output.txt', 'w') as outfile:
    json.dump(final_list, outfile)

for i, e in enumerate(final_list):
    if "(" in e['standard']['definition'] and "\n\n" in e['standard']['definition']:
        print(i,": ",e)
