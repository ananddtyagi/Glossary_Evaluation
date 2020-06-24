import urllib.request
from bs4 import BeautifulSoup
import sys


url = sys.argv[1]
# url = https://en.wikipedia.org/wiki/Glossary_of_calculus
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")

print(soup.findAll('dt', class_='glossary')[0].find(text=True))
print(''.join(soup.findAll('dd', class_='glossary')[0].findAll(text=True)))

terms = soup.findAll('dt', class_='glossary')
definitions = soup.findAll('dd', class_='glossary')

assert(len(terms) == len(definitions))

