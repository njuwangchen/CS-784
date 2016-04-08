import pickle
import random

import numpy
from py_stringmatching import simfunctions, tokenizers

# sys.stdout = open('file', 'w')

with open('prodID_dict1.pickle', 'rb') as handle:
	product_dict = pickle.load(handle)

with open('attributeName_productID_dict1.pickle', 'rb') as handle:
	attributeName_productID_dict = pickle.load(handle)

print product_dict['35496125']['GTIN']

match_dict = {}
f = open('elec_pairs_stage1.txt', 'r')
i = 1
for line in f:
	list_line = line.split('?')
	print(i)
	match_dict[(list_line[1], list_line[3])] = list_line[5].strip()
	i = i + 1
#	if (i > 10):
#		break
# pprint(match_dict)
f.close()

"""
with open('match_dict.pickle', 'wb') as handle:
	pickle.dump(match_dict, handle)

with open('match_dict.pickle', 'rb') as handle:
	b = pickle.load(handle)
print ( match_dict == b )
"""

# get feature vector X for 20k pairs (20k sample times n features) and there class labels y for 20k pairs
i = 0
feature_matrix = []
classlabels = []
id = []

for pair in match_dict:
	id1 = pair[0]
	id2 = pair[1]
	attribute_id1 = product_dict[id1]
	attribute_id2 = product_dict[id2]
	id.append([id1,id2])

	# class label
	if (match_dict[pair] == 'MATCH'):
		classlabels.append(1)
	else:
		classlabels.append(0)

	####feature: Product Type --- Jaccard Score (word boundary)
	if ("Product Type" in attribute_id1 and "Product Type" in attribute_id2):
		#print attribute_id2["Product Type"][0]
		jaccard_productType = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Type"][0]),tokenizers.delimiter(attribute_id2["Product Type"][0]))
		jaccard3gram_productType = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Type"][0], 3),tokenizers.qgram(attribute_id2["Product Type"][0], 3))
		tfidf_productType = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Type"][0]),tokenizers.delimiter(attribute_id2["Product Type"][0]))
	else:
		jaccard_productType = 0
		jaccard3gram_productType = 0
		tfidf_productType = 0
	# print jaccard_productType

	####feature: Product Segment --- Exact Match
	if "Product Segment" in attribute_id1 and "Product Segment" in attribute_id2:
		#print attribute_id1["Product Segment"][0]
		#print attribute_id2["Product Segment"][0]
		jaccard_productSegment = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Segment"][0]),tokenizers.delimiter(attribute_id2["Product Segment"][0]))
		jaccard3gram_productSegment= simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Segment"][0], 3),tokenizers.qgram(attribute_id2["Product Segment"][0], 3))
		if (attribute_id1["Product Segment"][0] == attribute_id2["Product Segment"][0]):
			exactMatch_productSegment = 1
		else:
			exactMatch_productSegment = 0

	else:
		exactMatch_productSegment = 0
		jaccard_productSegment = 0
		jaccard3gram_productSegment = 0

	####feature: Brand --- Jaccard Score (3-grams)
	if ("Brand" in attribute_id1 and "Brand" in attribute_id2):
		# print attribute_id1["Brand"][0]
		# print attribute_id2["Brand"][0]
		# print tokenizers.qgram(attribute_id1["Brand"][0],3)
		jaccard_brand = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Brand"][0]),tokenizers.delimiter(attribute_id2["Brand"][0]))
		jaccard3gram_brand = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Brand"][0], 3),
												  tokenizers.qgram(attribute_id2["Brand"][0], 3))
	else:  # if one brandname is missing
		jaccard3gram_brand = 0
		jaccard_brand = 0
	# print jaccard3gram_brand

	####feature: GTIN --- Exact Match
	if ("GTIN" in attribute_id1 and "GTIN" in attribute_id2):
		# print attribute_id1["GTIN"][0]
		# print attribute_id2["GTIN"][0]
		if (attribute_id1["GTIN"][0] == attribute_id2["GTIN"][0]):
			exactMatch_GTIN = 1
	else:
		exactMatch_GTIN = 0
	# print exactMatch_GTIN

	if ("UPC" in attribute_id1 and "UPC" in attribute_id2):
		# print attribute_id1["UPC"][0]
		# print attribute_id2["UPC"][0]
		if (attribute_id1["UPC"][0] == attribute_id2["UPC"][0]):
			exactMatch_UPC = 1
		else:
			exactMatch_UPC = 0
	else:
		exactMatch_UPC = 0
	# print exactMatch_UPC

	####feature: Category --- Jaccard Score (word boundary)

	if ("Category" in attribute_id1 and "Category" in attribute_id2):
		# print attribute_id1["Category"][0]
		# print attribute_id2["Category"][0]
		jaccard_category = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Category"][0]),
												tokenizers.delimiter(attribute_id2["Category"][0]))
		jaccard3gram_category = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Category"][0], 3),
												  tokenizers.qgram(attribute_id2["Category"][0], 3))
	else:
		jaccard_category = 0
		jaccard3gram_category = 0
		# print jaccard_category


	feature_matrix.append([jaccard_productType, tfidf_productType,jaccard3gram_productType, exactMatch_productSegment, jaccard3gram_brand,jaccard_brand, exactMatch_GTIN, exactMatch_UPC,jaccard_category,jaccard3gram_category])

	i = i + 1
#	if (i > 10):
#		break

# print feature_matrix
# print classlabels

all_index = range(len(classlabels))
random.seed(2)
index_for_test = random.sample(all_index, 10000)
index_for_train = list(set(all_index) - set(index_for_test))

classlabels_test = []
feature_matrix_test = []

for i in index_for_test:
	classlabels_test.append(classlabels[i])
	feature_matrix_test.append(feature_matrix[i])

classlabels_train = []
feature_matrix_train = []

for i in index_for_train:
	classlabels_train.append(classlabels[i])
	feature_matrix_train.append(feature_matrix[i])

k = 9900
id_tuning_100 = []
attribute_tuning_100 = []
label_tuning_100 = []

j=1
for i in index_for_train[-(10000-k):]:
	id_tuning_100.append(id[i])
	attribute_tuning_100.append([product_dict[id[i][0]],product_dict[id[i][1]]])
	label_tuning_100.append(classlabels[i])
	print j
	print "id1: %s, id2:%s, match: %d" %(id[i][0] , id[i][1] ,classlabels[i])
	print product_dict[id[i][0]]
	print product_dict[id[i][1]]
	print "***********************************8"
	j=j+1

"""
with open('id_tuning_100.pickle', 'wb') as handle:
	pickle.dump(id_tuning_100, handle)
with open('attribute_tuning_100.pickle', 'wb') as handle:
	pickle.dump(attribute_tuning_100, handle)
with open('label_tuning_100.pickle', 'wb') as handle:
	pickle.dump(label_tuning_100, handle)
"""
with open('classlabels_train.pickle', 'wb') as handle:
	pickle.dump(classlabels_train, handle)
with open('feature_matrix_train.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_train, handle)
with open('classlabels_test.pickle', 'wb') as handle:
	pickle.dump(classlabels_test, handle)
with open('feature_matrix_test.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_test, handle)





"""
print index_for_test
print classlabels
print classlabels_test
print feature_matrix
print feature_matrix_test
"""