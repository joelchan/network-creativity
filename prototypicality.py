import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np
import scipy.stats as stats

# define the x "bins" we will use for all the distributions
BUCKETS = np.linspace(0, 1, 10)

def compute_prototypical_distribution(idea_edge_weights):
    """Given a set of ideas (each represented as a list of edge_weights [output of ideas_to_edge_weights])
    return a prototypical distribution. Per toubia, average at each edge weight value across all ideas.
    """
    
    # initialize container for computing average cdf for each x
    all_cdfs = {}
    for b in BUCKETS:
        all_cdfs[b] = []

    # compute ecdf for each idea
    idea_edge_weights['cdf'] = ""
    for index, idea in idea_edge_weights.iterrows():
        # print idea['edge_weights']
        if len(idea['edge_weights']) > 0:
            # create the ecdf for the idea
            ecdf = ECDF(idea['edge_weights'])
            this_cdf = []
            for b in BUCKETS:
                this_cdf.append(ecdf(b))
                all_cdfs[b] += [ecdf(b)]
            idea_edge_weights.set_value(index, 'cdf', this_cdf)

    # compute the prototypical distribution by averaging across cdfs for each bucket
    proto_cdf = []
    for b in BUCKETS:
        proto_cdf.append(np.mean(all_cdfs[b]))
    
    return proto_cdf, idea_edge_weights

def idea_prototypicality(idea_edges, baseline_avg_cdf):
    """Given a set of edge weights (of ideas), compute a prototypicality score for each idea
    where prototypicality is defined as the Kolmogorov-Smirnov distance of the idea cdf from the average baseline cdf
    return a pandas data frame that has each idea id, idea content, and prototypicality score
    """
    
    idea_edges['prototypicality'] = 0.0
    idea_edges['cdf'] = ""
    for index, idea in idea_edges.iterrows():
        # compute the cdf
        if len(idea['edge_weights']) > 0:
            ecdf = ECDF(idea['edge_weights'])
            this_cdf = [ecdf(b) for b in BUCKETS]
            # estimate difference between idea cdf and baseline prototypical cdf
            ks = stats.ks_2samp(this_cdf, baseline_avg_cdf)[0]; # returns tuple of KS statistic (D) and p value
            idea_edges.set_value(index, 'cdf', this_cdf)
            idea_edges.set_value(index, 'prototypicality', ks)
    return idea_edges