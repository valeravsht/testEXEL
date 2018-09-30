#!/usr/local/bin/python

# -*- coding: utf8 -*-

if __name__ == '__main__':
    pass
import openpyxl
import os
import xlwt
import matplotlib
import pandas as pd

from itertools import groupby
#from main import minusword as mw
from myYandex.minusword import MinusWord 

#from MinusWord import *

s1 = pd.Series([1,2,3,4,5,6],)

# os.chdir('d:\\1')
# 
# df = pd.read_excel(open('15694565.xls','rb'),sheet_name='txt', encoding='utf-8')
# d=[]
# 
# print(df.keys())
# print(df['Unnamed: 2'])
# print(df.ix[18,'Unnamed: 3'])
# df.ix[18,'Unnamed: 3'] = 88888888
# print(df.ix[18,'Unnamed: 3'])
# print(df.shape)


# Initialize a workbook 
#book = xlwt.Workbook(encoding="utf-8")

# Add a sheet to the workbook 
#sheet1 = book.add_sheet("Python Sheet 1") 

# Write to the sheet of the workbook 
#sheet1.write(1, 2, "This is the First Cell of the First Sheet") 

# Save the workbook 
#book.save("spreadsheet.xls")
tire= [ [ "CONTINENTAL","ContiIceContact", '2' ,  "" ,  '175',    '65',    '14'],    
  ["CONTINENTAL"  ,  "ContiIceContact", '2' ,  "" ,  '185',    '65',    '15'],   
  ["CONTINENTAL",    "ContiIceContact" ,'2',   "" ,  '195',    '65',    '15'],    
  ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '215',    '65',    '16'],   
  ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '215' ,   '65',    '17'],   
  ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '225' ,   '65',    '17'],    
  ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '235' ,   '55',    '20'],    
  ["CONTINENTAL",    "ContiIceContact", '2', "SUV" , '245' ,   '55' ,   '19'],    
  ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '265' ,   '60' ,   '18']]   
word1 = ['шина зимняя','купить шина зимняя']

minusW = MinusWord.create(tire)
for key in minusW:
    print(minusW[key])


# 
# def createMinusWord(arrWord =[] ):
#     minusWord = {}
#     tmpstr = ''
#     for t in arrWord:
#         i=1
#         print(t)
#         for iw in t:
#             #print(iw)
#             tmpstr = ''
#             for tmpWord in t[:i]:
#                 tmpstr += tmpWord
#                 if tmpWord !=  t[:i][-1] and len(tmpWord)>0:#не последнее и не пустое
#                     tmpstr += " "
#             # print('!'+tmpstr+'!')     
#             #print(t[:i],t[i:])
#             for tmpMw in t[i:]:
#                 if len(tmpMw)>0:#не пустое
#                     minusWord[tmpstr].apend(tmpMw)
#             i+=1
#     # уберем дубликаты
#     for key in minusWord:
#         minusWord[key]=  [el for el, _ in groupby(minusWord[key])]        
#     return minusWord
        #print(tire[t][i]) 
#     
#     print("{0} -{1} -{2} -{3} -{4} -{5} -{6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#     print("{0} {1} -{2} -{3} -{4} -{5} -{6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#     print("{0} {1} {2} -{3} -{4} -{5} -{6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#     print("{0} {1} {2} {3} -{4} -{5} -{6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#     print("{0} {1} {2} {3} {4} -{5} -{6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#     print("{0} {1} {2} {3} {4} {5} -{6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#     print("{0} {1} {2} {3} {4} {5} {6}".format(tire[t][0],tire[t][1],tire[t][2],tire[t][3],tire[t][4],tire[t][5],tire[t][6]))
#                  
    # print("{0} {1} {2} {3} {4} {5} {6}".format(tire[t])) 

