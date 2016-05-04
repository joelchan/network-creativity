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

	training_ideas = pd.read_csv("data/fabric_120_creativity_scores.csv")
	test_ideas = pd.read_csv("data/fabric_display_all.csv")
	# test_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
	# test_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
	creativity_set = test_ideas["creativity"]
	# test_ideas, stem_frequencies = nlp.ideas_to_bow(test_ideas, 0)
	cumulative_correlation = pd.DataFrame([[0,0,0,0,0,0]], 
		columns = ['frequency_threshold', 'num_buckets','creativity','prototypicality','correlation', 'p-value'])

	for f_score in [1,2,3,4,5,10]:
		for num_buckets in [5,10,25,50,100]:

			# make the buckets
			this_buckets = np.linspace(0, 1, num_buckets)

			# import data and convert to bow representation
			print "Importing data..."
			# csv_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
			baseline_bow_ideas, stem_frequencies = nlp.ideas_to_bow(test_ideas, f_score)
			# bow_ideas.to_csv("stems_fabric_display_120_rand_trimmed.csv")

			# compute the baseline network
			# print "Computing edge weights..."
			stem_network = networks.ideas_to_stem_network(stem_frequencies.keys(), baseline_bow_ideas)
			# f = open("stem_network.json", 'w')
			# f.write(json.dumps(stem_network, indent=2))
			# f.close()

			# convert ideas to edge weights
			print "Converting ideas to edge weights"
			edge_ideas = networks.ideas_to_edge_weights(baseline_bow_ideas, stem_network)

			# compute baseline cdfs
			print "Computing baseline prototypical cdf..."
			baseline_cdf, cdf_ideas = pr.compute_prototypical_distribution(edge_ideas, this_buckets)

			print "Preprocessing test ideas..."
			test_bow_ideas, stem_frequencies = nlp.ideas_to_bow(test_ideas, f_score)
			this_test_ideas = networks.ideas_to_edge_weights(test_bow_ideas, stem_network)
			# compute prototypicality score
			print "Computing prototypicality scores..."
			pr_ideas = pr.idea_prototypicality(this_test_ideas, baseline_cdf, this_buckets)
			print pr_ideas.head(10)
			corr = stats.pearsonr(pr_ideas['prototypicality'], pr_ideas['creativity'])
			cumulative_correlation = cumulative_correlation.append(pd.DataFrame([[f_score, num_buckets, pr_ideas['creativity'], pr_ideas['prototypicality'], corr[0], corr[1]]], 
				columns = ['frequency_threshold', 'num_buckets','creativity','prototypicality','correlation', 'p-value']))
			# cumulative_correlation.append(pd.DataFrame())
		    # print stem_network
		    # print baseline_cdf
		    # cdf_ideas.to_csv("cdfs_fabric_display_5_rand.csv")

		    # re-represent test ideas as stem network edge weights
			# print "Processing test ideas..."
    # test_ideas = pd.read_csv("data/fabric_display_120_rand.csv")
    # test_ideas, stem_frequencies = nlp.ideas_to_bow(test_ideas, 0)
    		
	cumulative_correlation.to_csv("pr_120_trimmed.csv")
		    # print pr_ideas

		    # compute the idea cdfs
		        # call networks.ideas_to_network()
		        # call ideas_to_cdf()
		        # for measure prototypicality for each idea