import urllib.request
from bs4 import BeautifulSoup
import sys
import json
import pandas as pd

dict1 = pd.read_csv('electricity1.csv', deliminter='|')
print(dict1)