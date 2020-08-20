import wikipedia
import sys
import urllib.request
from bs4 import BeautifulSoup
import json
import os

def get_topic():
    #add a loop and a restart ability
    possible_topics = wikipedia.search(input('please enter a topic:\n'))
    #make sure a topic was entered
    for i, x in enumerate(possible_topics):
        print(i+1, ": ", x)
    topic_num = input("Please specify which topic you mean:\n")
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

    chosen = input("Please choose all the relavent subclasses (list each number separated by a comma (Ex. 1,3,4)):\n")

    if len(chosen) == 1:
        chosen_index = int(chosen)-1
        if chosen_index == len(categories):
            return [categories]
        else:
            return [categories[chosen_index]]

    selection = chosen.split(",")
    superclasses = []
    for x in selection:
        superclasses.append(categories[int(x)-1])

    return superclasses

def get_language():
    languages = ['English', 'Chinese', 'French']
    for i, cat in enumerate(languages):
        print(i+1, ': ', cat)

    lang_index = input('Please enter your language option (enter the number):""\n')
    lang_index = int(lang_index)-1
    return languages[lang_index]

def get_num_articles():
    return input('Please enter the number of articles you would like to search:\n')

def get_intermediate_file_path():
    return intput('Please enter the path respective to summary_from_2_terms.sh where you would like the intermeidate files to be made:\n')

def get_termolator_dir():
    return input('Please enter the location of the termolator with respect to the location of summary_from_2_terms.sh:\n')

def get_file_type():
    file_type = input("Please enter the type of file the summary should be written to (Ex. .txt, .xml, etc):/n")
    if file_type[0] != '.': #incase they don't add the dot
        file_type = '.' + file_type
    return file_type

def run_summary(superclasses, subclass):
    if sys.argv[1] == 'test':
        language = 'English'
        num_articles = '250'
        intermediate_file_path = '.'
        termolator_dir = '..'
        file_type = '.txt'
    else:
        language = get_language()
        num_articles = str(int(get_num_articles()) / len(superclasses)) #equal divide between superclasses
        intermediate_file_path = get_intermediate_file_path()
        termolator_dir = get_termolator_dir()
        file_type = get_file_type()

    os.system('bash '+ termolator_dir + '/wikipedia_file_extraction/get_wiki_corpus_main.sh '+ language +' '+ subclass +' '+ intermediate_file_path +'/'+ subclass +' True  '+ num_articles +' '+ termolator_dir +'/wikipedia_file_extraction')
    os.system('ls -1 '+ intermediate_file_path +'/'+ subclass +'/*'+ file_type +' > '+ intermediate_file_path +'/'+ subclass +'.file_list')

    os.system('touch '+ intermediate_file_path + '/'+ subclass + '_all_background_files.file_list')

    for super in superclasses:

        os.system('bash '+ termolator_dir + '/wikipedia_file_extraction/get_wiki_corpus_main.sh '+ language +' '+ super +' '+ intermediate_file_path +'/'+ super +' True  '+ num_articles +' '+ termolator_dir +'/wikipedia_file_extraction')
        print('making intermediate super')
        os.system('ls -1 '+ intermediate_file_path +'/'+super+'/*'+ file_type +' > '+ intermediate_file_path +'/'+ super +'.file_list')

        os.system('python3 '+ termolator_dir +'/make_glossary_part1.py '+ intermediate_file_path +'/'+ subclass +'.file_list '+ intermediate_file_path +'/'+ super +'.file_list  '+ subclass +' '+ super +' .txt '+ termolator_dir)

        os.system('cat '+ intermediate_file_path + '/'+  super + '.file_list >> '+ intermediate_file_path + '/'+ subclass + '_all_background_files.file_list')

    os.system(termolator_dir +'/run_termolator.sh '+ intermediate_file_path +'/'+ subclass +'.file_list_2 '+ intermediate_file_path + '/'+ subclass + '_all_background_files.file_list' +' .txt '+ subclass +' True True 30000 5000 '+ termolator_dir +' False False False wikipedia-$2.pkl -1')

    os.system(termolator_dir +'/run_term_map.sh '+ intermediate_file_path +'/'+ subclass +'.file_list_2 '+ intermediate_file_path +'/'+ subclass +'.out_term_list '+ subclass +' '+ intermediate_file_path +' '+ termolator_dir)

    os.system(termolator_dir +'/run_summary.sh '+ subclass +' '+ intermediate_file_path +' '+ termolator_dir +' .txt3')

    return

if argv[1] == 'test':
    subclass = 'COVID-19'
    superclasses = ['Viral_respiratory_tract_infections', 'Zoonotic_bacterial_diseases']
else:
    topic = get_topic()
    subclass = get_subclass(topic)
    superclasses = get_superclass(subclass)

run_summary(superclasses, subclass)