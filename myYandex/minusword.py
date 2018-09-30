'''
Created on 29 сент. 2018 г.

@author: valera
'''
from itertools import groupby

class MinusWord(object):
    '''
    classdocs
    '''

# 
#     def __init__(self, params):
#         '''
#         Constructor
#         '''
    @staticmethod    
    def create(arrWord =[] ):
        ''' Создает список ключевых слов и минусовых слов для массива
             такого вида
            [["CONTINENTAL","ContiIceContact", '2' ,  "" ,  '175',    '65',    '14'],    
            ["CONTINENTAL"  ,  "ContiIceContact", '2' ,  "" ,  '185',    '65',    '15'],   
            ["CONTINENTAL",    "ContiIceContact" ,'2',   "" ,  '195',    '65',    '15'],    
            ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '215',    '65',    '16'],   
            ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '215' ,   '65',    '17'],   
            ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '225' ,   '65',    '17'],    
            ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '235' ,   '55',    '20'],    
            ["CONTINENTAL",    "ContiIceContact", '2', "SUV" , '245' ,   '55' ,   '19'],    
            ["CONTINENTAL",    "ContiIceContact", '2', "SUV",  '265' ,   '60' ,   '18']]
              
        [    [0] -фирма
            [1,2,3] - модель по словам
            [4,5,6] - размер
        ]
        '''
        
        minusWord = {}
        tmpstr = ''
        for t in arrWord:
            i=1
            for iw in t:
                tmpstr = '' # для ключа словоря
                word = [] # масив для поисковых слов
                for tmpWord in t[:i]: # формируем поисковые слова
                    if tmpWord !=  t[:i][0] and len(tmpWord)>0:#не последнее и не пустое
                        tmpstr += " "    
                    if len(tmpWord)>0:# не пустое                    
                        tmpstr += tmpWord
                        word.append(tmpWord)

                if tmpstr not in minusWord: # новая поисковая фраза
                    minusWord[tmpstr]=[]
                    minusWord[tmpstr].append([])# 0 слова
                    minusWord[tmpstr].append([])# 1 минус слова        
                minusWord[tmpstr][0].append(word.copy())         
                for tmpMw in t[i:]: # формируем минусовые слова
                    if len(tmpMw)>0:#не пустое
                        minusWord[tmpstr][1].append(tmpMw)
              
                if tmpstr not in minusWord: # если нету минус слов
                    minusWord[tmpstr][1]=[]   
                          
                if iw != t[-1] and len(iw) >0 : # для запросов типа Continental 17
                    tmpstr += ' '
                    tmpstr += t[-1]
                    word.append(t[-1])
                    if tmpstr not in minusWord: # новая поисковая фраза
                        minusWord[tmpstr]=[]
                        minusWord[tmpstr].append([])# 0 слова
                        minusWord[tmpstr].append([])# 1 минус слова        
                    minusWord[tmpstr][0].append(word.copy())      
                    for tmpMw in t[i:]:
                        if len(tmpMw)>0 and tmpMw != t[-1]:#не пустое и не пос. диметр 
                            minusWord[tmpstr][1].append(tmpMw)
                i+=1
        # уберем дубликаты
        for key in minusWord:
            tmpList = minusWord[key][1].copy()
            tmpList.sort()
            tmpList1 = [el for el, _ in groupby(tmpList)] 
            minusWord[key][1]=  tmpList1.copy()      
        return minusWord   
    
   
    def comp(self,templ_list=[],sour_list=[]):
        '''
        сравнивает  список templ_list c sour_list
        если не пустые элементы масива равны возвращант  True
        иначе False
        '''
        #проверим на одинаковое число элементов
        if len(templ_list) != len(sour_list):
            return False
        ret = False
        i=0
        for templ in templ_list:
            if len(templ)>0:# не пустой элемент
                if templ == sour_list[i]:
                    ret = True
                else:
                    ret = False
            i+=1
                
        return ret
    
            