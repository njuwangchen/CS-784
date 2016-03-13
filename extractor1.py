from openpyxl import load_workbook
from random import shuffle
import codecs

def predictAndTest(productNamesSet, trueBrand):
    brand_predicted = []
    for productName in productNamesSet:
        list_words_in_productName = productName.split()
        brandFound = False

        if(not brandFound):
            for i in range(len(list_words_in_productName)-2):
                word_two_token = list_words_in_productName[i]+" "+list_words_in_productName[i+1]+" "+list_words_in_productName[i+2]
                if word_two_token.lower() in brand_dict:
                    brand_predicted.append(word_two_token)
                    brandFound = True
                    break
        if(not brandFound):
            for i in range(len(list_words_in_productName)-1):
                word_two_token = list_words_in_productName[i]+" "+list_words_in_productName[i+1]
                if word_two_token.lower() in brand_dict:
                    brand_predicted.append(word_two_token)
                    brandFound = True
                    break

        if(not brandFound):
            for word in list_words_in_productName:
                if word.lower() in brand_dict:
                    brand_predicted.append(word)
                    brandFound = True
                    break

        if(not brandFound):
            brand_predicted.append("None")

    count = 0
    for i in range(len(brand_predicted)):
        if(brand_predicted[i].lower() == trueBrand[i].lower()):
            count=count+1
        else:
            print "======" + productNamesSet[i]
            print brand_predicted[i]+","+trueBrand[i]
    return count

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
productNames = []
brandNames_true = []

productNames_test = []
brandNames_true_test = []
index_shuf = range(len(ProductName_sorted))
r=0.5  # shuffle use the same seed every time
shuffle(index_shuf,lambda: r)
shuffle(index_shuf,lambda: r)
shuffle(index_shuf,lambda: r)
#print index_shuf
for i in index_shuf[:120]:
    productNames_test.append(ProductName_sorted[i])
    brandNames_true_test.append(BrandName_true_sorted[i])
for i in index_shuf[120:]:
    productNames.append(ProductName_sorted[i])
    brandNames_true.append(BrandName_true_sorted[i])
    #print str(i)+","+BrandName_true[-1]+"==== "+ProductName[-1]
#print len(ProductName)
#print len(BrandName_true)

##### read the brand dictionary, key is the brand name( lower case), value is the frequency
brand_dict ={}
f = codecs.open('elec_brand_dic.txt', 'r', encoding='utf-8')

for line in f:
        list_line = line.split('\t')
        #brand_dict[list_line[0]]=int(list_line[1])
        brand_dict[list_line[0].lower()]=int(list_line[1])
        #print list_line
f.close()

correctNumOfTrain = predictAndTest(productNames, brandNames_true)
print correctNumOfTrain

correctNumOfTest = predictAndTest(productNames_test, brandNames_true_test)
print correctNumOfTest