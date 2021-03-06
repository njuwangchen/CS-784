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

    # if ("Product Short Description" in attribute_id2 and "Product Long Description" in attribute_id1):
    #     short_des_set = tokenizers.delimiter(attribute_id2["Product Short Description"][0])
    #     des = attribute_id1["Product Long Description"][0]
    #     count = 0
    #     for short in short_des_set:
    #         if short in des:
    #             count = count+1
    #     short2_in_des1 = count/len(short_des_set)
    # else:
    #     short2_in_des1 = 0
    #
    # feature_matrix_train[k].append(short2_in_des1)

    # if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     jaccard_short_description = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Short Description"][0]), tokenizers.delimiter(attribute_id2["Product Short Description"][0]))
    # else:
		# jaccard_short_description = 0
    #
    # feature_matrix_train[k].append(jaccard_short_description)
    #
    # if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     jaccard3_short_description = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Short Description"][0], 3), tokenizers.qgram(attribute_id2["Product Short Description"][0], 3))
    # else:
		# jaccard3_short_description = 0
    #
    # feature_matrix_train[k].append(jaccard3_short_description)

    # if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     tfidf_short_description = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Short Description"][0]), tokenizers.delimiter(attribute_id2["Product Short Description"][0]))
    # else:
    #     tfidf_short_description = 0
    #
    # feature_matrix_train[k].append(tfidf_short_description)
    #

    # if ("Product Name" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id1["Product Name"][0])
    #     des = attribute_id2["Product Short Description"][0]
    #     count = 0
    #     for name in name_set:
    #         if name in des:
    #             count = count+1
    #     name1_in_des2 = count/len(name_set)
    # else:
    #     name1_in_des2 = 0
    #
    # feature_matrix_train[k].append(name1_in_des2)
    #
    # if ("Product Short Description" in attribute_id1 and "Product Name" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id2["Product Name"][0])
    #     des = attribute_id1["Product Short Description"][0]
    #     count = 0
    #     for name in name_set:
    #         if name in des:
    #             count = count+1
    #     name2_in_des1 = count/len(name_set)
    # else:
    #     name2_in_des1 = 0
    #
    # feature_matrix_train[k].append(name2_in_des1)
    #
    # if ("Brand" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     brand_set = tokenizers.delimiter(attribute_id1["Brand"][0])
    #     des = attribute_id2["Product Short Description"][0]
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des:
    #             count = count+1
    #     brand1_in_des2 = count/len(brand_set)
    # else:
    #     brand1_in_des2 = 0
    #
    # feature_matrix_train[k].append(brand1_in_des2)
    #
    # if ("Brand" in attribute_id2 and "Product Short Description" in attribute_id1):
    #     brand_set = tokenizers.delimiter(attribute_id2["Brand"][0])
    #     des = attribute_id1["Product Short Description"][0]
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des:
    #             count = count+1
    #     brand2_in_des1 = count/len(brand_set)
    # else:
    #     brand2_in_des1 = 0
    #
    # feature_matrix_train[k].append(brand2_in_des1)
    #
    # if ("Manufacturer" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     manufacturer_set = tokenizers.delimiter(attribute_id1["Manufacturer"][0])
    #     des = attribute_id2["Product Short Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer1_in_des2 = count/len(manufacturer_set)
    # else:
    #     manufacturer1_in_des2 = 0
    #
    # feature_matrix_train[k].append(manufacturer1_in_des2)
    #
    # if ("Manufacturer" in attribute_id2 and "Product Short Description" in attribute_id1):
    #     manufacturer_set = tokenizers.delimiter(attribute_id2["Manufacturer"][0])
    #     des = attribute_id1["Product Short Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer2_in_des1 = count/len(manufacturer_set)
    # else:
    #     manufacturer2_in_des1 = 0
    #
    # feature_matrix_train[k].append(manufacturer2_in_des1)

    if ("Manufacturer Part Number" in attribute_id1 and "Product Long Description" in attribute_id2):
        manu_part_number_set = tokenizers.delimiter(attribute_id1["Manufacturer Part Number"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for manu_part in manu_part_number_set:
            if manu_part in des_set:
                count = count+1
        manu_part1_in_des2 = count/len(manu_part_number_set)
    else:
        manu_part1_in_des2 = 0

    feature_matrix_train[k].append(manu_part1_in_des2)

    if ("Manufacturer Part Number" in attribute_id2 and "Product Long Description" in attribute_id1):
        manu_part_number_set = tokenizers.delimiter(attribute_id2["Manufacturer Part Number"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for manu_part in manu_part_number_set:
            if manu_part in des_set:
                count = count+1
        manu_part2_in_des1 = count/len(manu_part_number_set)
    else:
        manu_part2_in_des1 = 0

    feature_matrix_train[k].append(manu_part2_in_des1)

    if ("Assembled Product Length" in attribute_id1 and "Product Long Description" in attribute_id2):
        length_set = tokenizers.delimiter(attribute_id1["Assembled Product Length"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for length in length_set:
            if length in des_set:
                count = count+1
        length1_in_des2 = count/len(length_set)
    else:
        length1_in_des2 = 0

    feature_matrix_train[k].append(length1_in_des2)

    if ("Assembled Product Length" in attribute_id2 and "Product Long Description" in attribute_id1):
        length_set = tokenizers.delimiter(attribute_id2["Assembled Product Length"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for length in length_set:
            if length in des_set:
                count = count+1
        length2_in_des1 = count/len(length_set)
    else:
        length2_in_des1 = 0

    feature_matrix_train[k].append(length2_in_des1)

    if ("Assembled Product Width" in attribute_id1 and "Product Long Description" in attribute_id2):
        width_set = tokenizers.delimiter(attribute_id1["Assembled Product Width"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for width in width_set:
            if width in des_set:
                count = count+1
        width1_in_des2 = count/len(width_set)
    else:
        width1_in_des2 = 0

    feature_matrix_train[k].append(width1_in_des2)

    if ("Assembled Product Width" in attribute_id2 and "Product Long Description" in attribute_id1):
        width_set = tokenizers.delimiter(attribute_id2["Assembled Product Width"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for width in width_set:
            if width in des_set:
                count = count+1
        width2_in_des1 = count/len(width_set)
    else:
        width2_in_des1 = 0

    feature_matrix_train[k].append(width2_in_des1)

    if ("Assembled Product Height" in attribute_id1 and "Product Long Description" in attribute_id2):
        height_set = tokenizers.delimiter(attribute_id1["Assembled Product Height"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for height in height_set:
            if height in des_set:
                count = count+1
        height1_in_des2 = count/len(height_set)
    else:
        height1_in_des2 = 0

    feature_matrix_train[k].append(height1_in_des2)

    if ("Assembled Product Height" in attribute_id2 and "Product Long Description" in attribute_id1):
        height_set = tokenizers.delimiter(attribute_id2["Assembled Product Height"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for height in height_set:
            if height in des_set:
                count = count+1
        height2_in_des1 = count/len(height_set)
    else:
        height2_in_des1 = 0

    feature_matrix_train[k].append(height2_in_des1)

    if ("Type" in attribute_id1 and "Product Long Description" in attribute_id2):
        type_set = tokenizers.delimiter(attribute_id1["Type"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for type in type_set:
            if type in des_set:
                count = count+1
        type1_in_des2 = count/len(type_set)
    else:
        type1_in_des2 = 0

    feature_matrix_train[k].append(type1_in_des2)

    if ("Type" in attribute_id2 and "Product Long Description" in attribute_id1):
        type_set = tokenizers.delimiter(attribute_id2["Type"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for type in type_set:
            if type in des_set:
                count = count+1
        type2_in_des1 = count/len(type_set)
    else:
        type2_in_des1 = 0

    feature_matrix_train[k].append(type2_in_des1)

    if ("Operating System" in attribute_id1 and "Product Long Description" in attribute_id2):
        op_set = tokenizers.delimiter(attribute_id1["Operating System"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for op in op_set:
            if op in op_set:
                count = count+1
        op1_in_des2 = count/len(op_set)
    else:
        op1_in_des2 = 0

    feature_matrix_train[k].append(op1_in_des2)

    if ("Operating System" in attribute_id2 and "Product Long Description" in attribute_id1):
        op_set = tokenizers.delimiter(attribute_id2["Operating System"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for op in op_set:
            if op in op_set:
                count = count+1
        op2_in_des1 = count/len(op_set)
    else:
        op2_in_des1 = 0

    feature_matrix_train[k].append(op2_in_des1)

    if ("Screen Size" in attribute_id1 and "Product Long Description" in attribute_id2):
        ss_set = tokenizers.delimiter(attribute_id1["Screen Size"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for ss in ss_set:
            if ss in ss_set:
                count = count+1
        ss1_in_des2 = count/len(ss_set)
    else:
        ss1_in_des2 = 0

    feature_matrix_train[k].append(ss1_in_des2)

    if ("Screen Size" in attribute_id2 and "Product Long Description" in attribute_id1):
        ss_set = tokenizers.delimiter(attribute_id2["Screen Size"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for ss in ss_set:
            if ss in ss_set:
                count = count+1
        ss2_in_des1 = count/len(ss_set)
    else:
        ss2_in_des1 = 0

    feature_matrix_train[k].append(ss2_in_des1)

    if "Product Long Description" in attribute_id2:
        all_set = []
        for key in attribute_id1:
            if key is not "Product Long Description":
                value_list = tokenizers.delimiter(attribute_id1[key][0])
                for v in value_list:
                    all_set.append(v)
        des = attribute_id2["Product Long Description"][0]
        count = 0
        for a in all_set:
            if a in des:
                count += 1
        all1_in_des2 = count/len(all_set)
    else:
        all1_in_des2 = 0

    feature_matrix_train[k].append(all1_in_des2)

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

    # if ("Product Short Description" in attribute_id2 and "Product Long Description" in attribute_id1):
    #     short_des_set = tokenizers.delimiter(attribute_id2["Product Short Description"][0])
    #     des = attribute_id1["Product Long Description"][0]
    #     count = 0
    #     for short in short_des_set:
    #         if short in des:
    #             count = count+1
    #     short2_in_des1 = count/len(short_des_set)
    # else:
    #     short2_in_des1 = 0
    #
    # feature_matrix_test[k].append(short2_in_des1)

    # if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     jaccard_short_description = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Short Description"][0]), tokenizers.delimiter(attribute_id2["Product Short Description"][0]))
    # else:
		# jaccard_short_description = 0
    #
    # feature_matrix_test[k].append(jaccard_short_description)
    #
    # if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     jaccard3_short_description = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Short Description"][0], 3), tokenizers.qgram(attribute_id2["Product Short Description"][0], 3))
    # else:
		# jaccard3_short_description = 0
    #
    # feature_matrix_test[k].append(jaccard3_short_description)

    # if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     tfidf_short_description = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Short Description"][0]), tokenizers.delimiter(attribute_id2["Product Short Description"][0]))
    # else:
    #     tfidf_short_description = 0
    #
    # feature_matrix_test[k].append(tfidf_short_description)

    # if ("Product Name" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id1["Product Name"][0])
    #     des = attribute_id2["Product Short Description"][0]
    #     count = 0
    #     for name in name_set:
    #         if name in des:
    #             count = count+1
    #     name1_in_des2 = count/len(name_set)
    # else:
    #     name1_in_des2 = 0
    #
    # feature_matrix_test[k].append(name1_in_des2)
    #
    # if ("Product Short Description" in attribute_id1 and "Product Name" in attribute_id2):
    #     name_set = tokenizers.delimiter(attribute_id2["Product Name"][0])
    #     des = attribute_id1["Product Short Description"][0]
    #     count = 0
    #     for name in name_set:
    #         if name in des:
    #             count = count+1
    #     name2_in_des1 = count/len(name_set)
    # else:
    #     name2_in_des1 = 0
    #
    # feature_matrix_test[k].append(name2_in_des1)
    #
    # if ("Brand" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     brand_set = tokenizers.delimiter(attribute_id1["Brand"][0])
    #     des = attribute_id2["Product Short Description"][0]
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des:
    #             count = count+1
    #     brand1_in_des2 = count/len(brand_set)
    # else:
    #     brand1_in_des2 = 0
    #
    # feature_matrix_test[k].append(brand1_in_des2)
    #
    # if ("Brand" in attribute_id2 and "Product Short Description" in attribute_id1):
    #     brand_set = tokenizers.delimiter(attribute_id2["Brand"][0])
    #     des = attribute_id1["Product Short Description"][0]
    #     count = 0
    #     for brand in brand_set:
    #         if brand in des:
    #             count = count+1
    #     brand2_in_des1 = count/len(brand_set)
    # else:
    #     brand2_in_des1 = 0
    #
    # feature_matrix_test[k].append(brand2_in_des1)
    #
    # if ("Manufacturer" in attribute_id1 and "Product Short Description" in attribute_id2):
    #     manufacturer_set = tokenizers.delimiter(attribute_id1["Manufacturer"][0])
    #     des = attribute_id2["Product Short Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer1_in_des2 = count/len(manufacturer_set)
    # else:
    #     manufacturer1_in_des2 = 0
    #
    # feature_matrix_test[k].append(manufacturer1_in_des2)
    #
    # if ("Manufacturer" in attribute_id2 and "Product Short Description" in attribute_id1):
    #     manufacturer_set = tokenizers.delimiter(attribute_id2["Manufacturer"][0])
    #     des = attribute_id1["Product Short Description"][0]
    #     count = 0
    #     for manufacturer in manufacturer_set:
    #         if manufacturer in des:
    #             count = count+1
    #     manufacturer2_in_des1 = count/len(manufacturer_set)
    # else:
    #     manufacturer2_in_des1 = 0
    #
    # feature_matrix_test[k].append(manufacturer2_in_des1)

    if ("Manufacturer Part Number" in attribute_id1 and "Product Long Description" in attribute_id2):
        manu_part_number_set = tokenizers.delimiter(attribute_id1["Manufacturer Part Number"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for manu_part in manu_part_number_set:
            if manu_part in des_set:
                count = count+1
        manu_part1_in_des2 = count/len(manu_part_number_set)
    else:
        manu_part1_in_des2 = 0

    feature_matrix_test[k].append(manu_part1_in_des2)

    if ("Manufacturer Part Number" in attribute_id2 and "Product Long Description" in attribute_id1):
        manu_part_number_set = tokenizers.delimiter(attribute_id2["Manufacturer Part Number"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for manu_part in manu_part_number_set:
            if manu_part in des_set:
                count = count+1
        manu_part2_in_des1 = count/len(manu_part_number_set)
    else:
        manu_part2_in_des1 = 0

    feature_matrix_test[k].append(manu_part2_in_des1)

    if ("Assembled Product Length" in attribute_id1 and "Product Long Description" in attribute_id2):
        length_set = tokenizers.delimiter(attribute_id1["Assembled Product Length"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for length in length_set:
            if length in des_set:
                count = count+1
        length1_in_des2 = count/len(length_set)
    else:
        length1_in_des2 = 0

    feature_matrix_test[k].append(length1_in_des2)

    if ("Assembled Product Length" in attribute_id2 and "Product Long Description" in attribute_id1):
        length_set = tokenizers.delimiter(attribute_id2["Assembled Product Length"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for length in length_set:
            if length in des_set:
                count = count+1
        length2_in_des1 = count/len(length_set)
    else:
        length2_in_des1 = 0

    feature_matrix_test[k].append(length2_in_des1)

    if ("Assembled Product Width" in attribute_id1 and "Product Long Description" in attribute_id2):
        width_set = tokenizers.delimiter(attribute_id1["Assembled Product Width"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for width in width_set:
            if width in des_set:
                count = count+1
        width1_in_des2 = count/len(width_set)
    else:
        width1_in_des2 = 0

    feature_matrix_test[k].append(width1_in_des2)

    if ("Assembled Product Width" in attribute_id2 and "Product Long Description" in attribute_id1):
        width_set = tokenizers.delimiter(attribute_id2["Assembled Product Width"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for width in width_set:
            if width in des_set:
                count = count+1
        width2_in_des1 = count/len(width_set)
    else:
        width2_in_des1 = 0

    feature_matrix_test[k].append(width2_in_des1)

    if ("Assembled Product Height" in attribute_id1 and "Product Long Description" in attribute_id2):
        height_set = tokenizers.delimiter(attribute_id1["Assembled Product Height"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for height in height_set:
            if height in des_set:
                count = count+1
        height1_in_des2 = count/len(height_set)
    else:
        height1_in_des2 = 0

    feature_matrix_test[k].append(height1_in_des2)

    if ("Assembled Product Height" in attribute_id2 and "Product Long Description" in attribute_id1):
        height_set = tokenizers.delimiter(attribute_id2["Assembled Product Height"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for height in height_set:
            if height in des_set:
                count = count+1
        height2_in_des1 = count/len(height_set)
    else:
        height2_in_des1 = 0

    feature_matrix_test[k].append(height2_in_des1)

    if ("Type" in attribute_id1 and "Product Long Description" in attribute_id2):
        type_set = tokenizers.delimiter(attribute_id1["Type"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for type in type_set:
            if type in des_set:
                count = count+1
        type1_in_des2 = count/len(type_set)
    else:
        type1_in_des2 = 0

    feature_matrix_test[k].append(type1_in_des2)

    if ("Type" in attribute_id2 and "Product Long Description" in attribute_id1):
        type_set = tokenizers.delimiter(attribute_id2["Type"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for type in type_set:
            if type in des_set:
                count = count+1
        type2_in_des1 = count/len(type_set)
    else:
        type2_in_des1 = 0

    feature_matrix_test[k].append(type2_in_des1)

    if ("Operating System" in attribute_id1 and "Product Long Description" in attribute_id2):
        op_set = tokenizers.delimiter(attribute_id1["Operating System"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for op in op_set:
            if op in op_set:
                count = count+1
        op1_in_des2 = count/len(op_set)
    else:
        op1_in_des2 = 0

    feature_matrix_test[k].append(op1_in_des2)

    if ("Operating System" in attribute_id2 and "Product Long Description" in attribute_id1):
        op_set = tokenizers.delimiter(attribute_id2["Operating System"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for op in op_set:
            if op in op_set:
                count = count+1
        op2_in_des1 = count/len(op_set)
    else:
        op2_in_des1 = 0

    feature_matrix_test[k].append(op2_in_des1)

    if ("Screen Size" in attribute_id1 and "Product Long Description" in attribute_id2):
        ss_set = tokenizers.delimiter(attribute_id1["Screen Size"][0])
        des_set = attribute_id2["Product Long Description"][0]
        count = 0
        for ss in ss_set:
            if ss in ss_set:
                count = count+1
        ss1_in_des2 = count/len(ss_set)
    else:
        ss1_in_des2 = 0

    feature_matrix_test[k].append(ss1_in_des2)

    if ("Screen Size" in attribute_id2 and "Product Long Description" in attribute_id1):
        ss_set = tokenizers.delimiter(attribute_id2["Screen Size"][0])
        des_set = attribute_id1["Product Long Description"][0]
        count = 0
        for ss in ss_set:
            if ss in ss_set:
                count = count+1
        ss2_in_des1 = count/len(ss_set)
    else:
        ss2_in_des1 = 0

    feature_matrix_test[k].append(ss2_in_des1)

    if "Product Long Description" in attribute_id2:
        all_set = []
        for key in attribute_id1:
            if key is not "Product Long Description":
                value_list = tokenizers.delimiter(attribute_id1[key][0])
                for v in value_list:
                    all_set.append(v)
        des = attribute_id2["Product Long Description"][0]
        count = 0
        for a in all_set:
            if a in des:
                count += 1
        all1_in_des2 = count/len(all_set)
    else:
        all1_in_des2 = 0

    feature_matrix_test[k].append(all1_in_des2)

    k = k+1

with open('classlabels_train.pickle', 'wb') as handle:
	pickle.dump(classlabels_train, handle)
with open('feature_matrix_train.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_train, handle)
with open('classlabels_test.pickle', 'wb') as handle:
	pickle.dump(classlabels_test, handle)
with open('feature_matrix_test.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_test, handle)

