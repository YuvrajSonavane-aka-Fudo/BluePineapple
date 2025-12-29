import re

def underScore(string1):
    string2 = re.findall(r"\b\w*_\w*\b", string1)
    print(string2)

underScore("_abc")