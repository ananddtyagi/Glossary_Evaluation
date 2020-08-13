import urllib.request
from bs4 import BeautifulSoup
import sys
import json

subclass = input('please enter the subclass topic\n')

url = "https://en.wikipedia.org/wiki/Category:" + subclass

try:
    page = urllib.request.urlopen(url)
except:
    print('This is not a valid subclass, please entere a valid category')
    sys.exit(1)
soup = BeautifulSoup(page, "lxml")

cat_section = soup.find(id='mw-normal-catlinks')
super_categories = []

for cat in cat_section.findAll('a')[1:]:
    super_categories.append(cat.text)

print('Here are a list of superclasses:')

for i, cat in enumerate(super_categories):
    print(i+1, ': ', cat)

cat_index = input('Please choose one (enter the number)\n')
cat_index = int(cat_index)-1

superclass = super_categories[cat_index]

languages = ['English', 'Chinese', 'French']
for i, cat in enumerate(languages):
    print(i+1, ': ', cat)

lang_index = input('Please enter your language option(enter the number)\n')
lang_index = int(lang_index)-1
language = languages[lang_index]

num_articles = input('Please enter the number of articles you would like to search\n')


subclass = subclass.replace(' ', '_')
superclass = superclass.replace(' ', '_')

print(' '.join(['../summary_from_2_terms.sh',subclass, superclass,'.',language,'..',num_articles,'.txt']))

