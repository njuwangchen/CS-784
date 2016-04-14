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

#brand_courpus = []

# for pair in match_dict:
#     id1 = pair[0]
#     id2 = pair[1]
#     attribute_id1 = product_dict[id1]
#     attribute_id2 = product_dict[id2]

    # if "Brand" in attribute_id1:
    #     brand_courpus.append(tokenizers.delimiter(attribute_id1["Brand"][0]))
    # if "Brand" in attribute_id2:
    #     brand_courpus.append(tokenizers.delimiter(attribute_id2["Brand"][0]))


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

    # if ("Brand" in attribute_id1 and "Brand" in attribute_id2):
    #     tfidf_brand = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Brand"][0]), tokenizers.delimiter(attribute_id2["Brand"][0]), brand_courpus)
    # else:
    #     tfidf_brand = 0
    #
    # feature_matrix_train[k].append(tfidf_brand)

    # if ("Product Name" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id1["Product Name"][0])
    #     des_set = tokenizers.delimiter(attribute_id2["Product Long Description"][0])
    #     count = 0
    #     for name in name_set:
    #         if name in des_set:
    #             count = count+1
    #     name1_in_des2 = count/len(name_set)
    # else:
    #     name1_in_des2 = 0
    #
    # feature_matrix_train[k].append(name1_in_des2)

    # if ("Product Long Description" in attribute_id1 and "Product Name" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id2["Product Name"][0])
    #     des_set = tokenizers.delimiter(attribute_id1["Product Long Description"][0])
    #     count = 0
    #     for name in name_set:
    #         if name in des_set:
    #             count = count+1
    #     name2_in_des1 = count/len(name_set)
    # else:
    #     name2_in_des1 = 0
    #
    # feature_matrix_train[k].append(name2_in_des1)

    # if ("Product Long Description" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     jaccard_long_description = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Long Description"][0]), tokenizers.delimiter(attribute_id2["Product Long Description"][0]))
    # else:
		# jaccard_long_description = 0
    #
    # feature_matrix_train[k].append(jaccard_long_description)

    # if ("Product Long Description" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     jaccard3_long_description = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Long Description"][0], 3), tokenizers.qgram(attribute_id2["Product Long Description"][0], 3))
    # else:
		# jaccard3_long_description = 0
    #
    # feature_matrix_train[k].append(jaccard3_long_description)

    # if ("Brand" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     brand_set = tokenizers.delimiter(attribute_id1["Brand"][0])
    #     des_set = tokenizers.delimiter(attribute_id2["Product Long Description"][0])
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des_set:
    #             count = count+1
    #     brand1_in_des2 = count/len(brand_set)
    # else:
    #     brand1_in_des2 = 0
    #
    # feature_matrix_train[k].append(brand1_in_des2)

    # if ("Brand" in attribute_id2 and "Product Long Description" in attribute_id1):
    #     brand_set = tokenizers.delimiter(attribute_id2["Brand"][0])
    #     des_set = tokenizers.delimiter(attribute_id1["Product Long Description"][0])
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des_set:
    #             count = count+1
    #     brand2_in_des1 = count/len(brand_set)
    # else:
    #     brand2_in_des1 = 0
    #
    # feature_matrix_train[k].append(brand2_in_des1)

    # if ("Manufacturer" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     manufacturer_set = tokenizers.delimiter(attribute_id1["Manufacturer"][0])
    #     des = attribute_id2["Product Long Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer1_in_des2 = count/len(manufacturer_set)
    # else:
    #     manufacturer1_in_des2 = 0
    #
    # feature_matrix_train[k].append(manufacturer1_in_des2)

    # if ("Manufacturer" in attribute_id2 and "Product Long Description" in attribute_id1):
    #     manufacturer_set = tokenizers.delimiter(attribute_id2["Manufacturer"][0])
    #     des = attribute_id1["Product Long Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer2_in_des1 = count/len(manufacturer_set)
    # else:
    #     manufacturer2_in_des1 = 0
    #
    # feature_matrix_train[k].append(manufacturer2_in_des1)

    # if ("Product Short Description" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     short_des_set = tokenizers.delimiter(attribute_id1["Product Short Description"][0])
    #     des = attribute_id2["Product Long Description"][0]
    #     count = 0
    #     for short in short_des_set:
    #         if short in des:
    #             count = count+1
    #     short1_in_des2 = count/len(short_des_set)
    # else:
    #     short1_in_des2 = 0
    #
    # feature_matrix_train[k].append(short1_in_des2)

    if ("Product Short Description" in attribute_id2 and "Product Long Description" in attribute_id1):
        short_des_set = tokenizers.delimiter(attribute_id2["Product Short Description"][0])
        des = attribute_id1["Product Long Description"][0]
        count = 0
        for short in short_des_set:
            if short in des:
                count = count+1
        short2_in_des1 = count/len(short_des_set)
    else:
        short2_in_des1 = 0

    feature_matrix_train[k].append(short2_in_des1)

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

    # if ("Brand" in attribute_id1 and "Brand" in attribute_id2):
    #     tfidf_brand = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Brand"][0]), tokenizers.delimiter(attribute_id2["Brand"][0]), brand_courpus)
    # else:
    #     tfidf_brand = 0
    #
    # feature_matrix_test[k].append(tfidf_brand)

    # if ("Product Name" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id1["Product Name"][0])
    #     des_set = tokenizers.delimiter(attribute_id2["Product Long Description"][0])
    #     count = 0
    #     for name in name_set:
    #         if name in des_set:
    #             count = count+1
    #     name1_in_des2 = count/len(name_set)
    # else:
    #     name1_in_des2 = 0
    #
    # feature_matrix_test[k].append(name1_in_des2)

    # if ("Product Long Description" in attribute_id1 and "Product Name" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id2["Product Name"][0])
    #     des_set = tokenizers.delimiter(attribute_id1["Product Long Description"][0])
    #     count = 0
    #     for name in name_set:
    #         if name in des_set:
    #             count = count+1
    #     name2_in_des1 = count/len(name_set)
    # else:
    #     name2_in_des1 = 0
    #
    # feature_matrix_test[k].append(name2_in_des1)

    # if ("Product Long Description" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     jaccard_long_description = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Long Description"][0]), tokenizers.delimiter(attribute_id2["Product Long Description"][0]))
    # else:
		# jaccard_long_description = 0
    #
    # feature_matrix_test[k].append(jaccard_long_description)

    # if ("Product Long Description" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     jaccard3_long_description = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Long Description"][0], 3), tokenizers.qgram(attribute_id2["Product Long Description"][0], 3))
    # else:
		# jaccard3_long_description = 0
    #
    # feature_matrix_test[k].append(jaccard3_long_description)

    # if ("Brand" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     brand_set = tokenizers.delimiter(attribute_id1["Brand"][0])
    #     des_set = tokenizers.delimiter(attribute_id2["Product Long Description"][0])
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des_set:
    #             count = count+1
    #     brand1_in_des2 = count/len(brand_set)
    # else:
    #     brand1_in_des2 = 0
    #
    # feature_matrix_test[k].append(brand1_in_des2)

    # if ("Brand" in attribute_id2 and "Product Long Description" in attribute_id1):
    #     brand_set = tokenizers.delimiter(attribute_id2["Brand"][0])
    #     des_set = tokenizers.delimiter(attribute_id1["Product Long Description"][0])
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des_set:
    #             count = count+1
    #     brand2_in_des1 = count/len(brand_set)
    # else:
    #     brand2_in_des1 = 0
    #
    # feature_matrix_test[k].append(brand2_in_des1)

    # if ("Manufacturer" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     manufacturer_set = tokenizers.delimiter(attribute_id1["Manufacturer"][0])
    #     des = attribute_id2["Product Long Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer1_in_des2 = count/len(manufacturer_set)
    # else:
    #     manufacturer1_in_des2 = 0
    #
    # feature_matrix_test[k].append(manufacturer1_in_des2)

    # if ("Manufacturer" in attribute_id2 and "Product Long Description" in attribute_id1):
    #     manufacturer_set = tokenizers.delimiter(attribute_id2["Manufacturer"][0])
    #     des = attribute_id1["Product Long Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer2_in_des1 = count/len(manufacturer_set)
    # else:
    #     manufacturer2_in_des1 = 0
    #
    # feature_matrix_test[k].append(manufacturer2_in_des1)

    # if ("Product Short Description" in attribute_id1 and "Product Long Description" in attribute_id2):
    #     short_des_set = tokenizers.delimiter(attribute_id1["Product Short Description"][0])
    #     des = attribute_id2["Product Long Description"][0]
    #     count = 0
    #     for short in short_des_set:
    #         if short in des:
    #             count = count+1
    #     short1_in_des2 = count/len(short_des_set)
    # else:
    #     short1_in_des2 = 0
    #
    # feature_matrix_test[k].append(short1_in_des2)

    if ("Product Short Description" in attribute_id2 and "Product Long Description" in attribute_id1):
        short_des_set = tokenizers.delimiter(attribute_id2["Product Short Description"][0])
        des = attribute_id1["Product Long Description"][0]
        count = 0
        for short in short_des_set:
            if short in des:
                count = count+1
        short2_in_des1 = count/len(short_des_set)
    else:
        short2_in_des1 = 0

    feature_matrix_test[k].append(short2_in_des1)

    k = k+1

with open('classlabels_train.pickle', 'wb') as handle:
	pickle.dump(classlabels_train, handle)
with open('feature_matrix_train.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_train, handle)
with open('classlabels_test.pickle', 'wb') as handle:
	pickle.dump(classlabels_test, handle)
with open('feature_matrix_test.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_test, handle)

