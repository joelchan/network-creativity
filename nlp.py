import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
import pandas as pd
import re

# THRESHOLD = 5 # frequency threshold for stems is variable in experiments, so we aren't keeping it as a global variable, 
# instead it's a varible passed into ideas_to_bow

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

def ideas_to_bow(raw_ideas, THRESHOLD):
    """Given text of ideas, convert to bag of words ("stems") representation
    Assume it's in a pandas df with columns [id, content]
    """

    stopwords = get_stopwords()

    # idea_stems = []
    raw_ideas['stems'] = ""
    frequency = {}

    for index, idea in raw_ideas.iterrows():

        # read the text
        text = idea['content'].encode('utf-8', 'ignore')

        # split into sentences (PunktSentenceTokenizer)
        sentences = nltk.sent_tokenize(text)

        # tokenize and stem the words with porter stemmer
        stemmer = PorterStemmer()
        stems = set() # NOTE: this is different from usual BOW because we only want the unique stems in the idea
        
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
        raw_ideas.set_value(index, 'stems', stems)
        # idea_stems.append({'id': idea['id'], 'content': idea['content'], 'stems': stems, 'creativity': idea['creativity']})
    
    # idea_stems = pd.DataFrame(idea_stems)
    # apply frequency filter (in Toubia, f >= 5 for ideas, and f >= 10 for Google results)
    all_frequency_trimmed = {}
    for index, idea in raw_ideas.iterrows():
        freq_trimmed = [stem for stem in idea['stems'] if frequency[stem] >= THRESHOLD]
        for word in freq_trimmed:
            all_frequency_trimmed[word] = frequency[word]
        raw_ideas.set_value(index, 'stems', freq_trimmed)
    # stems = [stem for stem in stems if frequency[stem] > THRESHOLD]

    return raw_ideas, all_frequency_trimmed