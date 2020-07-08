import json
from rouge import Rouge
# from tqdm import tqdm
import sys

rouge = Rouge()

datafile = sys.argv[1]

def read_input():
    file = open(datafile, "r")

    list_articles = json.load(file)

    return list_articles

def aggregate_scores(list_articles):

    rouge_l = {
        "r": 0,
        "p": 0,
        "f": 0
    }

    len_article = len(list_articles)
    skipped = 0
    total_used = 0
    # t = tqdm(list_articles, desc = 'Eval:')

    for i, obj in enumerate(list_articles):

        reference_sum = obj["reference"]
        system_sum = obj["system"]


        try:
            result = rouge.get_scores(system_sum, reference_sum)[0]

            rouge_l["r"] += result["rouge-l"]["r"]
            rouge_l["p"] += result["rouge-l"]["p"]
            rouge_l["f"] += result["rouge-l"]["f"]

            total_used += 1
        except ValueError:
            skipped += 1
            #Do nothing

    print("Final Scores")

    rouge_l["r"] = rouge_l["r"]/total_used
    rouge_l["p"] = rouge_l["p"]/total_used
    rouge_l["f"] = rouge_l["f"]/total_used

    print(datafile)
    print("Rouge-l")
    print(rouge_l)

def main():

    list_articles = read_input()

    max_ref = 0
    max_sys = 0

    nonevalues = 0

    for _, i in enumerate(list_articles):
        if len(i['reference']) > max_ref:
            max_ref = len(i['reference'])
        if len(i['system']) > max_sys:
            max_sys = len(i['system'])

    sys.setrecursionlimit(max_ref * max_sys + 10)

    aggregate_scores(list_articles)

main()