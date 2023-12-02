# Description
This system evaluates glossaries using the ROUGE-L evaluation metric.

# Running the program

## Scraping
For scraping the glossary off of the wikipedia glossary page, run the scraping program and pass the topic you are interested in as the first argument as such:

```
scraping.py <topic>
```
If there is a 404:Not Found error returned by urllib.error.HTTPError, unfortunately, that topic is not one currently supported.

## Evaluation
To run the evaluation, execute
```
evaluation.py <datafile>
```

The `<datafile>` should be a .txt file in json format with each entry having two parameters:

  reference: the answer key
  system: your system output

#Reference

This system was made by Anand Tyagi as a part of a research project conducted with NYU Professor Adam Meyers

