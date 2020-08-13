from didyoumean import didyoumean
import pickle

spell = input('enter the subclass\n')
pages = []

with open('../wiki-cats.list.pickle', 'rb') as handle:
    pages = pickle.load(handle)


correctSpell = didyoumean.didYouMean(spell, pages)
print(correctSpell)


while (input('would you like to search for a page?\n') == 'y'):

    query = input('enter the subclass\n')

    match = didyoumean.didYouMean(query, pages)
    if match == None:
        print('No match was found\n')
    elif match in pages:
        continue;
    else:
        resp = input('Did you mean ' +  match + '?\n')
        while resp == 'n':
            pages.remove(match)
            match = didyoumean.didYouMean(query, pages)
            if match == None:
                print('No other matches were found\n')
                break;
            else:
                resp = input('Did you mean ', match, '?\n')
