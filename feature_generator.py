__author__ = 'ClarkWong'
import json
import pickle
from py_stringmatching import simfunctions, tokenizers

def generate_feature(filename):
    productName_courpus = []
    brand_courpus = []
    with open(filename, 'r') as f:
        for line in f:
            list_line = line.split('?')
            attribute_id1 = json.loads(list_line[2], encoding = 'latin-1')
            attribute_id2 = json.loads(list_line[4], encoding = 'latin-1')

            if "Product Name" in attribute_id1:
		        productName_courpus.append(tokenizers.delimiter(attribute_id1["Product Name"][0]))
            if "Product Name" in attribute_id2:
                productName_courpus.append(tokenizers.delimiter(attribute_id2["Product Name"][0]))

            if "Brand" in attribute_id1:
                brand_courpus.append(tokenizers.delimiter(attribute_id1["Brand"][0]))
            if "Brand" in attribute_id2:
                brand_courpus.append(tokenizers.delimiter(attribute_id2["Brand"][0]))

    feature_matrix = []
    with open(filename, 'r') as f:
        i = 1
        for line in f:
            list_line = line.split('?')
            attribute_id1 = json.loads(list_line[2], encoding = 'latin-1')
            attribute_id2 = json.loads(list_line[4], encoding = 'latin-1')

            print 'Generate features for pair', i
            i = i+1

            instance = []

            #Product Name 4
            if ("Product Name" in attribute_id1 and "Product Name" in attribute_id2):
                jaccard_productName = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Name"][0]), tokenizers.delimiter(attribute_id2["Product Name"][0]))
                jaccard3gram_productName = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Name"][0], 3), tokenizers.qgram(attribute_id2["Product Name"][0], 3))
                tfidf_productName = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Name"][0]), tokenizers.delimiter(attribute_id2["Product Name"][0]), productName_courpus)
                edit_productName = simfunctions.levenshtein(attribute_id1["Product Name"][0], attribute_id2["Product Name"][0])
                edit_productName = 1 - edit_productName/max(len(attribute_id1["Product Name"][0]), len(attribute_id2["Product Name"][0]))
            else:
                jaccard_productName = 0
                jaccard3gram_productName = 0
                tfidf_productName = 0
                edit_productName = 0

            instance += [jaccard_productName, jaccard3gram_productName, tfidf_productName, edit_productName]

            #Manufacturer 3
            if ("Manufacturer" in attribute_id1 and "Manufacturer" in attribute_id2):
                jaccard_manufacturer = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Manufacturer"][0]), tokenizers.delimiter(attribute_id2["Manufacturer"][0]))
                jaccard3gram_manufacturer = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Manufacturer"][0], 3), tokenizers.qgram(attribute_id2["Manufacturer"][0], 3))
                tfidf_manufacturer = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Manufacturer"][0]), tokenizers.delimiter(attribute_id2["Manufacturer"][0]))
            else:
                jaccard_manufacturer = 0
                jaccard3gram_manufacturer = 0
                tfidf_manufacturer = 0

            instance += [jaccard_manufacturer, jaccard3gram_manufacturer, tfidf_manufacturer]

            #Color 3
            if ("Color" in attribute_id1 and "Color" in attribute_id2):
                jaccard_color = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Color"][0]), tokenizers.delimiter(attribute_id2["Color"][0]))
                jaccard3gram_color = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Color"][0], 3), tokenizers.qgram(attribute_id2["Color"][0], 3))
                tfidf_color = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Color"][0]), tokenizers.delimiter(attribute_id2["Color"][0]))
            else:
                jaccard_color = 0
                jaccard3gram_color = 0
                tfidf_color = 0

            instance += [jaccard_color, jaccard3gram_color, tfidf_color]

            #Product Type 3
            if ("Product Type" in attribute_id1 and "Product Type" in attribute_id2):
                jaccard_productType = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Type"][0]),tokenizers.delimiter(attribute_id2["Product Type"][0]))
                jaccard3gram_productType = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Type"][0], 3),tokenizers.qgram(attribute_id2["Product Type"][0], 3))
                tfidf_productType = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Type"][0]),tokenizers.delimiter(attribute_id2["Product Type"][0]))
            else:
                jaccard_productType = 0
                jaccard3gram_productType = 0
                tfidf_productType = 0

            instance += [jaccard_productType, jaccard3gram_productType, tfidf_productType]

            #Product Segment 3
            if "Product Segment" in attribute_id1 and "Product Segment" in attribute_id2:
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

            instance += [exactMatch_productSegment, jaccard_productSegment, jaccard3gram_productSegment]

            #Brand 4
            if ("Brand" in attribute_id1 and "Brand" in attribute_id2):
                jaccard_brand = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Brand"][0]),tokenizers.delimiter(attribute_id2["Brand"][0]))
                jaccard3gram_brand = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Brand"][0], 3),
                                                          tokenizers.qgram(attribute_id2["Brand"][0], 3))
                edit_brand = simfunctions.levenshtein(attribute_id1["Brand"][0], attribute_id2["Brand"][0])
                edit_brand = 1 - edit_brand/max(len(attribute_id1["Brand"][0]), len(attribute_id2["Brand"][0]))
                tfidf_brand = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Brand"][0]), tokenizers.delimiter(attribute_id2["Brand"][0]), brand_courpus)
            else:
                jaccard3gram_brand = 0
                jaccard_brand = 0
                edit_brand = 0
                tfidf_brand = 0

            instance += [jaccard_brand, jaccard3gram_brand, edit_brand, tfidf_brand]

            #Category 2
            if ("Category" in attribute_id1 and "Category" in attribute_id2):
                jaccard_category = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Category"][0]),
                                                        tokenizers.delimiter(attribute_id2["Category"][0]))
                jaccard3gram_category = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Category"][0], 3),
                                                          tokenizers.qgram(attribute_id2["Category"][0], 3))
            else:
                jaccard_category = 0
                jaccard3gram_category = 0

            instance += [jaccard_category, jaccard3gram_category]

            #Long Description 3
            if ("Product Long Description" in attribute_id1 and "Product Long Description" in attribute_id2):
                tfidf_long_description = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Long Description"][0]), tokenizers.delimiter(attribute_id2["Product Long Description"][0]))
                jaccard_long_description = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Long Description"][0]), tokenizers.delimiter(attribute_id2["Product Long Description"][0]))
                jaccard3_long_description = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Long Description"][0], 3), tokenizers.qgram(attribute_id2["Product Long Description"][0], 3))
            else:
                tfidf_long_description = 0
                jaccard_long_description = 0
                jaccard3_long_description = 0

            instance += [tfidf_long_description, jaccard_long_description, jaccard3_long_description]

            #Short Description 3
            if ("Product Short Description" in attribute_id1 and "Product Short Description" in attribute_id2):
                jaccard_short_description = simfunctions.jaccard(tokenizers.delimiter(attribute_id1["Product Short Description"][0]), tokenizers.delimiter(attribute_id2["Product Short Description"][0]))
                jaccard3_short_description = simfunctions.jaccard(tokenizers.qgram(attribute_id1["Product Short Description"][0], 3), tokenizers.qgram(attribute_id2["Product Short Description"][0], 3))
                tfidf_short_description = simfunctions.tfidf(tokenizers.delimiter(attribute_id1["Product Short Description"][0]), tokenizers.delimiter(attribute_id2["Product Short Description"][0]))
            else:
                jaccard_short_description = 0
                jaccard3_short_description = 0
                tfidf_short_description = 0

            instance += [jaccard_short_description, jaccard3_short_description, tfidf_short_description]

            #Other in long 8
            if ("Product Name" in attribute_id1 and "Product Long Description" in attribute_id2):
                name_set = tokenizers.delimiter(attribute_id1["Product Name"][0])
                des = attribute_id2["Product Long Description"][0]
                count = 0
                for name in name_set:
                    if name in des:
                        count = count+1
                name1_in_des2 = count/len(name_set)
            else:
                name1_in_des2 = 0

            instance += [name1_in_des2]

            if ("Product Long Description" in attribute_id1 and "Product Name" in attribute_id2):
                name_set = tokenizers.delimiter(attribute_id2["Product Name"][0])
                des = attribute_id1["Product Long Description"][0]
                count = 0
                for name in name_set:
                    if name in des:
                        count = count+1
                name2_in_des1 = count/len(name_set)
            else:
                name2_in_des1 = 0

            instance += [name2_in_des1]

            if ("Brand" in attribute_id1 and "Product Long Description" in attribute_id2):
                brand_set = tokenizers.delimiter(attribute_id1["Brand"][0])
                des = attribute_id2["Product Long Description"][0]
                count = 0
                for brand in brand_set:
                    if brand in des:
                        count = count+1
                brand1_in_des2 = count/len(brand_set)
            else:
                brand1_in_des2 = 0

            instance += [brand1_in_des2]

            if ("Brand" in attribute_id2 and "Product Long Description" in attribute_id1):
                brand_set = tokenizers.delimiter(attribute_id2["Brand"][0])
                des = attribute_id1["Product Long Description"][0]
                count = 0
                for brand in brand_set:
                    if brand in des:
                        count = count+1
                brand2_in_des1 = count/len(brand_set)
            else:
                brand2_in_des1 = 0

            instance += [brand2_in_des1]

            if ("Manufacturer" in attribute_id1 and "Product Long Description" in attribute_id2):
                manufacturer_set = tokenizers.delimiter(attribute_id1["Manufacturer"][0])
                des = attribute_id2["Product Long Description"][0]
                count = 0
                for manufacturer in manufacturer_set:
                    if manufacturer in des:
                        count = count+1
                manufacturer1_in_des2 = count/len(manufacturer_set)
            else:
                manufacturer1_in_des2 = 0

            instance += [manufacturer1_in_des2]

            if ("Manufacturer" in attribute_id2 and "Product Long Description" in attribute_id1):
                manufacturer_set = tokenizers.delimiter(attribute_id2["Manufacturer"][0])
                des = attribute_id1["Product Long Description"][0]
                count = 0
                for manufacturer in manufacturer_set:
                    if manufacturer in des:
                        count = count+1
                manufacturer2_in_des1 = count/len(manufacturer_set)
            else:
                manufacturer2_in_des1 = 0

            instance += [manufacturer2_in_des1]

            if ("Product Short Description" in attribute_id1 and "Product Long Description" in attribute_id2):
                short_des_set = tokenizers.delimiter(attribute_id1["Product Short Description"][0])
                des = attribute_id2["Product Long Description"][0]
                count = 0
                for short in short_des_set:
                    if short in des:
                        count = count+1
                short1_in_des2 = count/len(short_des_set)
            else:
                short1_in_des2 = 0

            instance += [short1_in_des2]

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

            instance += [short2_in_des1]

            #Other in short 6
            if ("Product Name" in attribute_id1 and "Product Short Description" in attribute_id2):
                name_set = tokenizers.delimiter(attribute_id1["Product Name"][0])
                des = attribute_id2["Product Short Description"][0]
                count = 0
                for name in name_set:
                    if name in des:
                        count = count+1
                name1_in_short2 = count/len(name_set)
            else:
                name1_in_short2 = 0

            instance += [name1_in_short2]

            if ("Product Short Description" in attribute_id1 and "Product Name" in attribute_id2):
                name_set = tokenizers.delimiter(attribute_id2["Product Name"][0])
                des = attribute_id1["Product Short Description"][0]
                count = 0
                for name in name_set:
                    if name in des:
                        count = count+1
                name2_in_short1 = count/len(name_set)
            else:
                name2_in_short1 = 0

            instance += [name2_in_short1]

            if ("Brand" in attribute_id1 and "Product Short Description" in attribute_id2):
                brand_set = tokenizers.delimiter(attribute_id1["Brand"][0])
                des = attribute_id2["Product Short Description"][0]
                count = 0
                for brand in brand_set:
                    if brand in des:
                        count = count+1
                brand1_in_short2 = count/len(brand_set)
            else:
                brand1_in_short2 = 0

            instance += [brand1_in_short2]

            if ("Brand" in attribute_id2 and "Product Short Description" in attribute_id1):
                brand_set = tokenizers.delimiter(attribute_id2["Brand"][0])
                des = attribute_id1["Product Short Description"][0]
                count = 0
                for brand in brand_set:
                    if brand in des:
                        count = count+1
                brand2_in_short1 = count/len(brand_set)
            else:
                brand2_in_short1 = 0

            instance += [brand2_in_short1]

            if ("Manufacturer" in attribute_id1 and "Product Short Description" in attribute_id2):
                manufacturer_set = tokenizers.delimiter(attribute_id1["Manufacturer"][0])
                des = attribute_id2["Product Short Description"][0]
                count = 0
                for manufacturer in manufacturer_set:
                    if manufacturer in des:
                        count = count+1
                manufacturer1_in_short2 = count/len(manufacturer_set)
            else:
                manufacturer1_in_short2 = 0

            instance += [manufacturer1_in_short2]

            if ("Manufacturer" in attribute_id2 and "Product Short Description" in attribute_id1):
                manufacturer_set = tokenizers.delimiter(attribute_id2["Manufacturer"][0])
                des = attribute_id1["Product Short Description"][0]
                count = 0
                for manufacturer in manufacturer_set:
                    if manufacturer in des:
                        count = count+1
                manufacturer2_in_short1 = count/len(manufacturer_set)
            else:
                manufacturer2_in_short1 = 0

            instance += [manufacturer2_in_short1]

            feature_matrix.append(instance)

    return feature_matrix

def generate_label(filename):
    classlabels = []
    with open(filename, 'r') as f:
        i = 1
        for line in f:
            print 'generate label for pair', i
            i += 1
            list_line = line.split('?')
            label = list_line[5].strip()
            if (label == 'MATCH'):
                classlabels.append(1)
            else:
                classlabels.append(0)

    return classlabels

feature_matrix_train = generate_feature('elec_pairs_stage3.txt')
classlabels_train = generate_label('elec_pairs_stage3.txt')

feature_matrix_predict = generate_feature('elec_pairs_stage3_test1.txt')

with open('feature_matrix_train_20000.pickle', 'wb') as handle:
	pickle.dump(feature_matrix_train, handle)

with open('classlabels_train_20000.pickle', 'wb') as handle:
    pickle.dump(classlabels_train, handle)

with open('feature_matrix_predict.pickle', 'wb') as handle:
    pickle.dump(feature_matrix_predict, handle)

