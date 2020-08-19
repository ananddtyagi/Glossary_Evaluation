#take subclass from that page
#use that subclass to perform get_superclass
#have user choose from the multiple superclass
#run equal split of articles with each different superclass
#modify shell file summary_from_2_terms to handle multiple superclasses

import wikipedia
import sys
import urllib.request
from bs4 import BeautifulSoup
import json

def get_topic():
    #add a loop and a restart ability
    possible_topics = wikipedia.search(input('please enter a topic:\n'))
    #make sure a topic was entered
    for i, x in enumerate(possible_topics):
        print(i+1, ": ", x)
    topic_num = input("Please specify which topic you mean\n")
    #check that topic num is a valid int
    topic_num = int(topic_num)
    return possible_topics[topic_num-1]

def get_subclass(topic):
    topic = topic.replace(" ", "_")
    url = "https://en.wikipedia.org/wiki/" + topic
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, "lxml")

    cat_section = soup.find(id='mw-normal-catlinks')
    categories = []

    for cat in cat_section.findAll('a')[1:]:
        categories.append(cat.text)

    return categories[0]

def get_superclass(subclass):

    subclass = subclass.replace(" ", "_")
    url = "https://en.wikipedia.org/wiki/Category:" + subclass
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, "lxml")

    cat_section = soup.find(id='mw-normal-catlinks')
    categories = []

    for cat in cat_section.findAll('a')[1:]:
        categories.append(cat.text)

    for i, x in enumerate(categories):
        print(i+1, ": ", x)
    print(len(categories) + 1, ":  All")

    chosen = input("Please choose all the relavent subclasses (list each number separated by a comma (Ex. 1,3,4))\n")

    if len(chosen) == 1:
        chosen_index = int(chosen)-1
        if chosen_index == len(categories):
            return categories
        else:
            return categories[chosen_index]

    selection = chosen.split(",")
    superclasses = []
    for x in selection:
        superclasses.append(categories[int(x)-1])

    return superclasses

def run_summary(superclasses, subclass):

    return

topic = get_topic()
subclass = get_subclass(topic)
superclasses = get_superclass(subclass)
run_summary(superclasses, subclass)