import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np
import scipy.stats as stats

# define the x "bins" we will use for all the distributions
BUCKETS = np.linspace(0, 1, 10)

def compute_prototypical_distribution(idea_bow, edge_weights):
    """Given a set of ideas (each represented as a list of stems [output of ideas_to_bow])
    and edge weights [output of ideas_to_stem_network],
    return a prototypical distribution
    """
    
    # initialize container for computing average cdf for each x
    all_cdfs = {}
    for b in BUCKETS:
        all_cdfs[b] = []

    # compute ecdf for each idea
    idea_bow['cdf'] = ""
    for index, idea in idea_edges():
        # create the ecdf for the idea
        ecdf = ECDF(idea['edges'])
        this_cdf = []
        for b in BUCKETS:
            this_cdf.append(ecdf(b))
            all_cdfs[b] += [ecdf(b)]
        idea_bow.set_value(index, 'cdf', this_cdf)

    # compute the prototypical distribution by averaging across cdfs for each bucket
    proto_cdf = []
    for b in BUCKETS:
        proto_cdf.append(np.mean(prototypical[b]))
    
    return ideas_bow, proto_cdf
