import pickle

filename = 'wiki-cats.txt'

dict = []

with open(filename) as f:
    for line in f.readlines():
        try:
            value = line.split("'")[1]
            dict.append(value)
        except:
            print(line)

with open(filename + 'list.pickle', 'wb') as handle:
    pickle.dump(dict, handle)

