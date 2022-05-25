# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import re


def read_file_content(filename):
    with open(filename, encoding = 'utf-8') as f:
        return f.read()

def count_words():

    text = read_file_content("./story.txt")
    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9 ]", "",text)
    text = text.split()

    unique_words = list(set(text))

    dict ={}

    for word in unique_words:
        no_of_occ = text.count(word)
        dict[word] = no_of_occ

    return dict

print(count_words())
