import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
import pandas as pd
import re

THRESHOLD = 10 # frequency threshold for stems

def read_data(filename):
    """
    Read in data from a file and return a list with each element being one line from the file.
    Parameters:
    1) filename: name of file to be read from
    Note: the code now opens as a binary and replaces carriage return characters with newlines because python's read and readline functions don't play well with carriage returns.
    However, this will no longer be an issue with python 3.
    """
    with open(filename, "rb") as f:
        s = f.read().replace('\r\n', '\n').replace('\r', '\n')
        data = s.split('\n')
    return data

def get_stopwords():
    """Returns a list of stop words. Currently uses a list of words in
    a text file

    """
    return read_data("englishstopwords-jc.txt")

def ideas_to_bow(raw_ideas):
    """Given text of ideas, convert to bag of words ("stems") representation
    Assume it's in a pandas df with columns [id, content]
    """

    stopwords = get_stopwords()

    idea_stems = []
    for index, idea in raw_ideas.iterrows():

        # read the text
        text = idea['content'].encode('utf-8', 'ignore')

        # split into sentences (PunktSentenceTokenizer)
        sentences = nltk.sent_tokenize(text)

        # tokenize and stem the words with porter stemmer
        stemmer = PorterStemmer()
        stems = set() # NOTE: this is different from usual BOW because we only want the unique stems in the idea
        frequency = {}
        for sentence in sentences:
            tokens = [token.lower() for token in nltk.word_tokenize(sentence) if token not in stopwords]  # tokenize
            for token in tokens:
                stem = stemmer.stem(token)
                if re.match('^[a-zA-Z0-9]+$', stem):
                    if stem in frequency:
                        frequency[stem] += 1
                    else:
                        frequency[stem] = 1
                    stems.add(stem)
        idea_stems.append({'id': idea['id'], 'content': idea['content'], 'stems': stems})
        # apply frequency filter (in Toubia, f >= 5 for ideas, and f >= 10 for Google results)
    # stems = [stem for stem in stems if frequency[stem] > THRESHOLD]
        

    return pd.DataFrame(idea_stems)