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
from myYandex.minusword import MinusWord,Tire 

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
  
listWord1 = ['шины зимние -купить -цена','купить шины зимние', 'шины зимние цена','шины -зимние -купить -цена','резина зимняя -купить -цена',
             'купить резину зимнею', 'резина зимнея цена' ]


'''
icecontact,
contivikingcontact,vikingcontact, viking contact,

contiwintercontact ,wintercontact
'''
tire1=[]

#переведем все в нижний регистр
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]=t_new[1].lower()
        #   t_new[2]=""
        t_new[4]=t_new[4].lower()
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())
        
# уберем 2 и suv       
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]=t_new[1].lower()
        t_new[2]=""
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())
        
# заменим ContiIceContact  на    icecontact
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]='icecontact'
        t_new[2]=""
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())

# заменим ContiIceContact  на    contivikingcontact
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]='contivikingcontact'
        t_new[2]=""
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())   
        
# заменим ContiIceContact  на    vikingcontact
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]='vikingcontact'
        t_new[2]=""
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())
           
# заменим ContiIceContact  на    viking contact
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]='viking'
        t_new[2]="contact"
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())
           
# заменим ContiIceContact  на    contiwintercontact
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]='contiwintercontact'
        t_new[2]=""
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy())   
        
# заменим ContiIceContact  на    wintercontact
for t in tire:
    a = MinusWord.comp( ['CONTINENTAL',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        t_new[0]=t_new[0].lower()
        t_new[1]='wintercontact'
        t_new[2]=""
        t_new[4]=''
        #  t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire1.append(t_new.copy()) 
        
tire2 = []
          
# добавим еще и r диметр
for t in tire1:
    a = MinusWord.comp( ['continental',"", '' ,  "" ,  '',    '',    ''],t)
    if a:
        t_new = t.copy()
        tire2.append(t.copy())  
        t_new[6] = 'r'+t_new[6]
        print(t_new)
        tire2.append(t_new.copy()) 
        
print(len(tire2))   

minusW = MinusWord.create(tire2)

print(len(minusW)) 

''' Фраза (с минус-словами) -  Unnamed: 8
    Заголовок 1                Unnamed: 11  
    Заголовок 2                Unnamed: 12 
    Текст                      Unnamed: 13
    Ссылка                     Unnamed: 17
    Отображаемая ссылка        Unnamed: 18
'''
    
os.chdir('d:\\1')
 
df = pd.read_excel(open('direct_example.xls','rb'),sheet_name='txt', encoding='utf-8')
d=[]

df2=df.ix[9].copy()

for word1 in listWord1:
    for word2 in minusW:
        df2.ix[ 'Unnamed: 8'] = ' ' + word1 + ' ' +  " ".join(minusW[word2][0]) + ' -' + " -".join(minusW[word2][1]) 
        df2.ix[ 'Unnamed: 11'] = 'Акция! Бесплатный шиномонтаж на шины Continental' 
        df2.ix[ 'Unnamed: 12'] = 'Достоверно. Додротно. Доступно.' 
        df2.ix[ 'Unnamed: 13'] = 'Доступные цены. Акция Бесплатный шиномонтаж на шины Contintntal'
        str_url = MinusWord.create_url(minusW[word2][2])
        df2.ix[ 'Unnamed: 17'] = 'http://shintorg.pro'  + str_url
        df = df.append(df2.copy())

# df2.ix[ 'Unnamed: 8'] = 'fpodspof poipiwerpo -jelej'
# df2.ix[ 'Unnamed: 11'] = 'УРА'
# df2.ix[ 'Unnamed: 12'] = 'Ууря' 
# df = df.append(df2.copy())
# df2.ix[ 'Unnamed: 8'] = 'fpodspof poipiwerpo -jelej!!!!!!!!!!!!!'
# df2.ix[ 'Unnamed: 11'] = 'УРА!!!!!!!!!!!!!!'
# df2.ix[ 'Unnamed: 12'] = 'Ууря!!!!!!!!!!!!!' 
# df = df.append(df2.copy())
#  
# print(df.keys())
# print(df['Unnamed: 2'])
# print(df.ix[18,'Unnamed: 3'])
# df.ix[18,'Unnamed: 3'] = 88888888
# print(df.ix[18,'Unnamed: 3'])
print(df.shape)
df.to_excel('d:\\1\\contic.xls', index=False)

print('Все')

