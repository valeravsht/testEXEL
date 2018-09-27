'''
@author: valera
'''
# -*- coding: utf8 -*-

if __name__ == '__main__':
    pass
import openpyxl
import os
import xlwt
import matplotlib
import pandas as pd

s1 = pd.Series([1,2,3,4,5,6],)

os.chdir('d:\\1')

df = pd.read_excel(open('15694565.xls','rb'),sheet_name='txt', encoding='utf-8')
d=[]

print(df.keys())
print(df['Unnamed: 2'])
print(df.ix[18,'Unnamed: 3'])
df.ix[18,'Unnamed: 3'] = 88888888
print(df.ix[18,'Unnamed: 3'])
print(df.shape)
# Initialize a workbook 
#book = xlwt.Workbook(encoding="utf-8")

# Add a sheet to the workbook 
#sheet1 = book.add_sheet("Python Sheet 1") 

# Write to the sheet of the workbook 
#sheet1.write(1, 2, "This is the First Cell of the First Sheet") 

# Save the workbook 
#book.save("spreadsheet.xls")