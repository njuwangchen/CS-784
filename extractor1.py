from openpyxl import load_workbook
wb = load_workbook('Samples_clean.xlsx')
ws = wb.active

# read the golden data from the excel file
ProductName_sorted=[];
for cellObj in ws.columns[1]:
        ProductName_sorted.append(str(cellObj.value))
BrandName_true_sorted=[];
for cellObj in ws.columns[2]:
        BrandName_true_sorted.append(str(cellObj.value))
# No brand read as "None"

####shuffle
from random import shuffle
productNames = []
brandNames_true = []
index_shuf = range(len(ProductName_sorted))
r=0.5  # shuffle use the same seed every time
shuffle(index_shuf,lambda: r)
shuffle(index_shuf,lambda: r)
shuffle(index_shuf,lambda: r)
#print index_shuf
for i in index_shuf:
    productNames.append(ProductName_sorted[i])
    brandNames_true.append(BrandName_true_sorted[i])
    #print str(i)+","+BrandName_true[-1]+"==== "+ProductName[-1]
#print len(ProductName)
#print len(BrandName_true)

##### read the brand dictionary, key is the brand name( lower case), value is the frequency
brand_dict ={}
#f = open('elec_brand_dic.txt', 'r')
import codecs
f = codecs.open('elec_brand_dic.txt', 'r', encoding='utf-8')

for line in f:
        list_line = line.split('\t')
        #brand_dict[list_line[0]]=int(list_line[1])
        brand_dict[list_line[0].lower()]=int(list_line[1])
        #print list_line
f.close()
#print len(brand_dict)
from pprint import pprint
#pprint(brand_dict)

#### tokenize each product name on word level and see if any token is in the dictionary
brand_predicted = []
for productName in productNames:
    list_words_in_productName = productName.split()
    #print productName
    #print list_words_in_productName
    brandFound = False
    for word in list_words_in_productName:
        if word.lower() in brand_dict:
            brand_predicted.append(word)
            brandFound = True
            break
    if(not brandFound):
        brand_predicted.append("None")

count = 0
for i in range(0,len(brand_predicted)):
    if(brand_predicted[i] == brandNames_true[i]):
        count=count+1
    else:
        print brand_predicted[i]+","+brandNames_true[i]
print count
#print brand_predicted
#print brandNames_true

# pay attention to lower case: lower case for dictionary dict
# pay attention to brandname with 2 words
# generate candidate set if multiple matches