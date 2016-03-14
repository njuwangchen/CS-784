# -*- coding: utf-8 -*-
__author__ = 'ClarkWong'
import json
import pickle
import random
import xlwt

product_dict = {}
product_list = []

f = open('elec_pairs_stage2.txt', 'r')

i = 1
for line in f:
    print "reading line", i
    i = i+1
    list_line = line.split('?')

    productID = list_line[1]
    productInfo = json.loads(list_line[2], encoding = 'latin-1')
    product_dict[productID] = productInfo
    productName = productInfo[u'Product Name']
    productTuple = (productID, productName)
    product_list.append(productTuple)

f.close()

with open('prodID_dict_s2.pickle', 'wb') as handle:
    pickle.dump(product_dict, handle)

sample_idx = [random.randint(0, 10000) for r in range(100)]
samples = []
for r in sample_idx:
    print product_list[r]
    samples.append(product_list[r])

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sample1")

row = 0
for i in samples:
    sheet.write(row, 0, i[0])
    sheet.write(row, 1, i[1])
    row=row+1

workbook.save("Samples_100.xls")








