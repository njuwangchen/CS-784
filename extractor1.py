from openpyxl import load_workbook
wb = load_workbook('Samples_clean.xlsx')
ws = wb.active

ProductName_sorted=[];
for cellObj in ws.columns[1]:
        ProductName_sorted.append(str(cellObj.value))

BrandName_true_sorted=[];
for cellObj in ws.columns[2]:
        BrandName_true_sorted.append(str(cellObj.value))
# No brand read as "None"

from random import shuffle
ProductName = []
BrandName_true = []
index_shuf = range(len(ProductName_sorted))
r=0.5  # shuffle use the same seed every time
shuffle(index_shuf,lambda: r)
shuffle(index_shuf,lambda: r)
shuffle(index_shuf,lambda: r)
print index_shuf
for i in index_shuf:
    ProductName.append(ProductName_sorted[i])
    BrandName_true.append(BrandName_true_sorted[i])
    print str(i)+","+BrandName_true[-1]+"==== "+ProductName[-1]


#print ProductName
#print BrandName_true
#print wb['sheet1']
#print ws.get_sheet_names()
#cell_range = ws['A1':'C2']
#print ws['A1'].value

#for i in range(1, 351):
        #print(i, ws.cell(row=i, column=2).value)


#for row in ws.iter_rows():
#    print row

# check out the last row
#for cell in row:
#    print cell