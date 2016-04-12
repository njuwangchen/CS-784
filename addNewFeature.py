__author__ = 'ClarkWong'

import pickle
import random

from py_stringmatching import simfunctions, tokenizers

with open('classlabels_train.pickle', 'rb') as handle:
	classlabels_train = pickle.load(handle)
with open('feature_matrix_train.pickle', 'rb') as handle:
	feature_matrix_train = pickle.load(handle)
with open('classlabels_test.pickle', 'rb') as handle:
	classlabels_test = pickle.load(handle)
with open('feature_matrix_test.pickle', 'rb') as handle:
	feature_matrix_test = pickle.load(handle)

with open('prodID_dict1.pickle', 'rb') as handle:
	product_dict = pickle.load(handle)

match_dict = {}
f = open('elec_pairs_stage3.txt', 'r')
i = 1
for line in f:
	list_line = line.split('?')
	match_dict[(list_line[1], list_line[3])] = list_line[5].strip()
	i = i + 1
f.close()

all_index = range(len(match_dict))
random.seed(2)
index_for_test = random.sample(all_index, 10000)
index_for_train = list(set(all_index) - set(index_for_test))

pair_keys = match_dict.keys()

k = 0
for i in index_for_train:
    print 'train', k
    pair = pair_keys[i]
    id1 = pair[0]
    id2 = pair[1]
    attribute_id1 = product_dict[id1]
    attribute_id2 = product_dict[id2]

    # if ("Brand" in attribute_id1 and "Brand" in attribute_id2):
    #     edit_brand = simfunctions.levenshtein(attribute_id1["Brand"][0], attribute_id2["Brand"][0])
    #     edit_brand = 1 - edit_brand/max(len(attribute_id1["Brand"][0]), len(attribute_id2["Brand"][0]))
    # else:
    #     edit_brand = 0
    #
    # feature_matrix_train[k].append(edit_brand)

    k = k+1

k = 0
for i in index_for_test:
    print 'test', k
    pair = pair_keys[i]
    id1 = pair[0]
    id2 = pair[1]
    attribute_id1 = product_dict[id1]
    attribute_id2 = product_dict[id2]

    # if ("Brand" in attribute_id1 and "Brand" in attribute_id2):
    #     edit_brand = simfunctions.levenshtein(attribute_id1["Brand"][0], attribute_id2["Brand"][0])
    #     edit_brand = 1 - edit_brand/max(len(attribute_id1["Brand"][0]), len(attribute_id2["Brand"][0]))
    # else:
    #     edit_brand = 0
    #
    # feature_matrix_test[k].append(edit_brand)
    k = k+1


with open('classlabels_train.pickle', 'wb') as handle:
	pickle.dump(classlabels_train, handle)
with open('feature_matrix_train.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_train, handle)
with open('classlabels_test.pickle', 'wb') as handle:
	pickle.dump(classlabels_test, handle)
with open('feature_matrix_test.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_test, handle)

