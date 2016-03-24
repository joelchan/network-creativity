from __future__ import division
from sklearn.metrics import jaccard_similarity_score
import itertools as it
import pandas as pd

def ideas_to_stem_network(stems, ideas_bow):
    """Given a set of ideas in bag of words (stems) form and a vocabulary set of stem nodes, 
    compute edge weights between all possible stem pairs
    where edge weights are given by the Jaccard index
    Store as numpy matrix?

    stems (list) - set of all stems used in the idea corpus
    ideas_bow (pandas DataFrame) - set of ideas in stem format (with ids)

    """

    edge_weights = {} # to store the edge weights

    # first compute idea set for each stem
    stem_sets = {}
    for s in stems:
        stem_sets[s] = in_ideas(s, ideas_bow)

    # compute network for all possible stem pairs
    for A, B in it.combinations(stems, 2):
        # create canonical (sorted) pair name
        pair = "-".join(sorted([A, B]))
        # if this not an identity match, and we haven't seen the pair already
        if A != B and pair not in edge_weights:
            # check the jaccard sim and add to edge weights
            weight = compute_edge(A, B, stem_sets)
            # print (A, B, weight)
            # if weight > 0:
            edge_weights[pair] = weight
                
        # print len(edge_weights)
    return edge_weights

def ideas_to_edge_weights(ideas_bow, edge_weights):
    """Given a set of ideas and the list of edge weights,
    Return a re-representation of each idea as a list of edge weights
    """

    ideas_bow['edge_weights'] = ""
    for index, idea in ideas_bow.iterrows():
        if len(idea['stems']) > 1: # sometimes ideas end up only having one stem, which makes combinatinos undefined
            this_edge_weights = []
            for A, B in it.combinations(idea['stems'], 2):
                pair = "-".join(sorted([A, B]))
                this_edge_weights.append(edge_weights[pair])
            ideas_bow.set_value(index, 'edge_weights', this_edge_weights)
        else:
            ideas_bow.set_value(index, 'edge_weights', [])
    return ideas_bow

def in_ideas(node, ideas_bow):
    """Find set of ideas that contain the node
    """
    containers = set()
    for index, row in ideas_bow.iterrows():
        if node in row['stems']:
            containers.add(row['id'])
    return containers

def compute_edge(A, B, stem_sets):
    """Compute edge between a pair of nodes (stems) A and B using Jaccard index
    """

    # Find SA - set of ideas that contain A
    SA = stem_sets[A]
    # Find SB - set of ideas that contain B
    SB = stem_sets[B]
    
    # jaccard is ratio of intersection(SA, SB) to union(SA, SB)
    return len(SA.intersection(SB)) / (len(SA.union(SB)))