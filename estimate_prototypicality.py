from __future__ import division
import pandas as pd
import numpy as np
import scipy as sp
import scipy.stats as stats
import nlp
import networks
import prototypicality as pr
from statsmodels.distributions.empirical_distribution import ECDF
import json
    
if __name__ == "__main__":

    # import data and convert to bow representation
    print "Importing data..."
    csv_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
    bow_ideas, stem_frequencies = nlp.ideas_to_bow(csv_ideas)
    bow_ideas.to_csv("stems_fabric_display_120_rand.csv")

    # compute the baseline network
    print "Computing edge weights..."
    stem_network = networks.ideas_to_stem_network(stem_frequencies.keys(), bow_ideas)
    f = open("stem_network.json", 'w')
    f.write(json.dumps(stem_network, indent=2))
    f.close()

    # convert ideas to edge weights
    print "Converting ideas to edge weights"
    edge_ideas = networks.ideas_to_edge_weights(bow_ideas, stem_network)

    # compute baseline cdfs
    print "Computing baseline prototypical cdf..."
    baseline_cdf, cdf_ideas = pr.compute_prototypical_distribution(edge_ideas)
    # print stem_network
    # print baseline_cdf
    # cdf_ideas.to_csv("cdfs_fabric_display_5_rand.csv")

    # re-represent test ideas as stem network edge weights
    print "Processing test ideas..."
    test_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
    test_ideas, stem_frequencies = nlp.ideas_to_bow(test_ideas)
    test_ideas = networks.ideas_to_edge_weights(test_ideas, stem_network)

    # compute prototypicality score
    print "Computing prototypicality scores..."
    pr_ideas = pr.idea_prototypicality(test_ideas, baseline_cdf)
    pr_ideas.to_csv("pr_120.csv")
    # print pr_ideas

    # compute the idea cdfs
        # call networks.ideas_to_network()
        # call ideas_to_cdf()
        # for measure prototypicality for each idea