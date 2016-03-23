from __future__ import division
import pandas as pd
import numpy as np
import scipy as sp
import scipy.stats as stats
import nlp
import networks
import prototypicality as pr
from statsmodels.distributions.empirical_distribution import ECDF

def cdf_an_idea(idea_nw):
    """Given an idea represented as edge weights, return its empirical cdf
    """
    # draw from statsmodels ECDF
    return None

def ideas_to_cdf(idea_bow, idea_network):
    """Expect result of nlp.ideas_to_network(), i.e., a set of ideas represented as edge weights
    Return a set of cdfs for each idea
    """


def average_distribution(ideas_cdf):
    """Given a set of cdfs, compute an average cdf.
    This is for creating the baseline "prototypical" distribution.
    Per toubia, average at each edge weight value across all ideas.
    """
    return None


    
if __name__ == "__main__":

    # import data and convert to bow representation
    csv_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
    bow_ideas, stem_frequencies = nlp.ideas_to_bow(csv_ideas)

    # compute the baseline network
    stem_network = networks.ideas_to_stem_network(stem_frequencies.keys(), bow_ideas)

    # convert ideas to edge weights
    edge_ideas = networks.ideas_to_edge_weights(bow_ideas, stem_network)

    # compute baseline cdfs
    baseline_cdf, cdf_ideas = pr.compute_prototypical_distribution(edge_ideas)
    # print stem_network
    # print baseline_cdf
    # cdf_ideas.to_csv("cdfs_fabric_display_5_rand.csv")

    # re-represent test ideas as stem network edge weights
    test_ideas = pd.read_csv("data/fabric_display_5_rand.csv")
    test_ideas, stem_frequencies = nlp.ideas_to_bow(test_ideas)
    test_ideas = networks.ideas_to_edge_weights(test_ideas, stem_network)

    # compute prototypicality score for 
    pr_ideas = idea_prototypicality(test_ideas, baseline_cdf)
    # print pr_ideas

    # compute the idea cdfs
        # call networks.ideas_to_network()
        # call ideas_to_cdf()
        # for measure prototypicality for each idea