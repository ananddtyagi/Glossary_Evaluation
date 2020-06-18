#Description
This system evaluates glossaries using the ROUGE-L evaluation metric.

#Running the program
To run the evaluation, run
```
evaluation.py <datafile>
```

The `<datafile>` should be a .txt file in json format with each entry having two parameters:

  reference: the answer key
  system: your system output

#Reference

This system was made by Anand Tyagi as a part of a research project conducted with NYU Professor Adam Meyers

