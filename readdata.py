# -*- coding: utf-8 -*-
import json
from pprint import pprint
import operator
import pickle

product_dict={}
attributeName_productID_dict={}

#f = open('sample.txt', 'r')
f = open('elec_pairs_stage3.txt', 'r')
i=1
for line in f:
    #print type(line)
    #print line
	#line.encode('utf-8')
	list_line = line.split('?')
    #print list_line;
    #print type(list_line[2])
    #print list_line[1]
    #print list_line[3]
    #print type(json.loads(list_line[2]))
    #print json.loads(list_line[2])
	print(i)
	i=i+1
	productID = list_line[1]
	product_dict[productID] = json.loads(list_line[2], encoding = 'latin-1')
	for attribute in json.loads(list_line[2], encoding = 'latin-1'):
        #print attribute
		if(attributeName_productID_dict.has_key(attribute)):
			if(productID not in attributeName_productID_dict[attribute]):
				attributeName_productID_dict[attribute].append(productID)
		else:
			attributeName_productID_dict[attribute]=[productID]

	productID = list_line[3]
	#print list_line[4]
	product_dict[productID] = json.loads(list_line[4], encoding = 'latin-1')
	for attribute in json.loads(list_line[4], encoding = 'latin-1'):
		if(attributeName_productID_dict.has_key(attribute)):
			#print ~(productID in attributeName_productID_dict[attribute])
			#print attributeName_productID_dict[attribute]
			#print productID
			if(productID not in attributeName_productID_dict[attribute]):
				attributeName_productID_dict[attribute].append(productID)
		else:
			attributeName_productID_dict[attribute]=[productID]

#print product_dict['34972919'].keys()
#print product_dict
#print attributeName_productID_dict
f.close()


"""
with open('prodID_dict.pickle', 'wb') as handle:
	pickle.dump(product_dict, handle)
with open('prodID_dict.pickle', 'rb') as handle:
	b = pickle.load(handle)
print ( product_dict == b )

with open('attributeName_productID_dict.pickle', 'wb') as handle:
	pickle.dump(attributeName_productID_dict, handle)
with open('attributeName_productID_dict.pickle', 'rb') as handle:
	c = pickle.load(handle)
print ( attributeName_productID_dict == c )
"""

with open('prodID_dict1.pickle', 'wb') as handle:
	pickle.dump(product_dict, handle)
with open('prodID_dict1.pickle', 'rb') as handle:
	b = pickle.load(handle)
print ( product_dict == b )

with open('attributeName_productID_dict1.pickle', 'wb') as handle:
	pickle.dump(attributeName_productID_dict, handle)
with open('attributeName_productID_dict1.pickle', 'rb') as handle:
	c = pickle.load(handle)
print ( attributeName_productID_dict == c )









