from __future__ import division
import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import kstest
import nlp
import networks
from statsmodels.distributions.empirical_distribution import ECDF

def cdf_an_idea(idea_nw):
    """Given an idea represented as edge weights, return its empirical cdf
    """
    # draw from statsmodels ECDF
    return None

def ideas_to_cdf(idea_network):
    """Expect result of nlp.ideas_to_network(), i.e., a set of ideas represented as edge weights
    Return a set of cdfs for each idea
    """

def average_distribution(ideas_cdf):
    """Given a set of cdfs, compute an average cdf.
    This is for creating the baseline "prototypical" distribution.
    Per toubia, average at each edge weight value across all ideas.
    """
    return None

def idea_prototypicality(ideas_cdf, baseline_avg_cdf):
    """Given a set of cdfs (of ideas), compute a prototypicality score for each idea
    where prototypicality is defined as the Kolmogorov-Smirnov distance of the idea cdf from the average baseline cdf
    return a pandas data frame that has each idea id, idea content, and prototypicality score
    """
    ideas_p = []
    for idea in ideas_cdf.iterrows():
        # estimate difference between idea cdf and baseline prototypical cdf
        ks = kstest(idea['cdf'], baseline_avg_cdf)[0]; # kstest returns tuple of KS statistic and p value
        ideas_p.append({'id': idea['id'], 'prototypicality': ks})
    # convert to dataframe
    ideas_p = pd.DataFrame(ideas_p)
    return ideas_p
    
if __name__ == "__main__":

    """
    TODO now for Varun
    """
    print "running"
    csv_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
    bow_ideas, stem_frequencies = nlp.ideas_to_bow(csv_ideas)
    stem_freq_keys = stem_frequencies.keys()
    # reduced_stem_frequencies = {}
    # for i in range(25): 
    #	reduced_stem_frequencies[stem_freq_keys[i]] = stem_frequencies[stem_freq_keys[i]]
    # stem_network = networks.ideas_to_stem_network(bow_ideas, reduced_stem_frequencies.keys())
    stem_network = networks.ideas_to_stem_network(bow_ideas, stem_frequencies.keys())
    # bow_ideas.to_csv("data/bow_csv.csv")
    # use pandas to import csv file

    # convert to bow representation (using nlp.ideas_to_bow())

    # export to csv

    """
    For later
    """
    #(idea_id, idea_content, prototypicality_score) = idea_prototypicality(ideas_cdf)
    #network = networks.ideas_to_network(idea_content)
    #new_ideas_cdf = ideas_to_cdf(idea_content)
 	#avg_dist = average_distribution(new_ideas_cdf)

    # create the baseline cdf
        # call networks.ideas_to_network()
        # call ideas_to_cdf()
        # call average_distribution()



    #return(prototypicality_score, avg_dist)

    # compute the idea cdfs
        # call networks.ideas_to_network()
        # call ideas_to_cdf()
        # for measure prototypicality for each idea