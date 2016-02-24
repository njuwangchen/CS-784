import json
from pprint import pprint
import operator
import pickle
import sys
import csv
sys.stdout = open('file', 'w')

with open('prodID_dict.pickle', 'rb') as handle:
	product_dict = pickle.load(handle)

with open('attributeName_productID_dict.pickle', 'rb') as handle:
	attributeName_productID_dict = pickle.load(handle)

#print len(str(product_dict['37670472']['Product Long Description']))


# + The list of all attributes that you find in the data.
#print attributeName_productID_dict.keys()
#print len(attributeName_productID_dict.keys())

# Top ten attribute
numberOfProduct = len(product_dict)
#print numberOfProduct
MissingValuePercent ={}
numberOfOccurences = {}

for attributeName in attributeName_productID_dict:
    #print str(attributeName) + "   " + str(len(attributeName_productID_dict[attributeName]))
    numberOfOccurences[attributeName] = len(attributeName_productID_dict[attributeName])
    MissingValuePercent[attributeName] =1-len(attributeName_productID_dict[attributeName])*1.0/numberOfProduct
    #print attributeName + str(1-len(attributeName_productID_dict[attributeName])*1.0/numberOfProduct)

#print len(attributeName_productID_dict['Product Name'])
#pprint(MissingValuePercent)
sorted_numberOfOcurences = sorted(numberOfOccurences.items(), key=operator.itemgetter(1),reverse=True)
print "AttributeName,   numberOfProducts"
#pprint(sorted_numberOfOcurences)
sorted_MissingValue = sorted(MissingValuePercent.items(), key=operator.itemgetter(1))

print "Top ten frequent attribute: sort by MissingValuePercentage"
#print len(str(product_dict['37670472']['Product Long Description']))

for a in sorted_MissingValue[0:10]:
	#print "%s , %f, {0:.0f}%", (a[0],a[1],a[1])
	print str(a[0])+"\t \t "+str(a[1])+"\t" + "{0:.3f}%".format(a[1]*100)

#pprint (sorted_MissingValue[0:10])


## print the top 10 attribute and its value for all products
## dictionary key=prodID, value = list of 10 attribute values 
#print len(str(product_dict['37670472']['Product Long Description']))

prodID_topAttributes_dict = {}
for prodID, att_dict in product_dict.iteritems():
	l = list()
	for attribute in sorted_MissingValue[0:10]:
		attributeName = attribute[0]
		if (attributeName in att_dict):
			l.append(att_dict[attributeName])
		else:
			l.append("")
	prodID_topAttributes_dict[prodID]=l
			
#print prodID_topAttributes_dict

#print len(str(product_dict['37670472']['Product Long Description']))

with open("topTenAttributes_all.csv", "wb") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(prodID_topAttributes_dict.keys())
   writer.writerows(zip(*prodID_topAttributes_dict.values()))

prodID_topAttributes_dict = {}
			
#print prodID_topAttributes_dict

# texture length average

#print len(str(product_dict['37670472']['Product Long Description']))

attribute_value_dict={}
for attribute in sorted_MissingValue[0:10]:
	attributeName = attribute[0]
	l = list()
	for prodID,att_dict in product_dict.iteritems():
		if attributeName in att_dict:
			#print str(prodID) +" "+str(attributeName) +" "+str(att_dict[attributeName])
			l.append(len(str(att_dict[attributeName])))
			
	attribute_value_dict[attributeName]=l


#pprint(attribute_value_dict)

print "\n length"
for attribute,l in attribute_value_dict.iteritems():
	print str(attribute)+"\t min:"+str(min(l)) + "\t max:"+ str(max(l)) + "\t mean:"+ str(sum(l)*1.0/len(l))
# histogram and csv

