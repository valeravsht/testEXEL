'''
Created on 29 сент. 2018 г.

@author: valera
'''
from itertools import groupby
from  myYandex.minusword import *


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
            
            tmpList = minusWord[key][0].copy()
            tmpList.sort()
            tmpList1 = [el for el, _ in groupby(tmpList)] 
            minusWord[key][0]=  tmpList1.copy()   
        
        #уберем лишний уровень масивов
        for key in minusWord:
            tmpList = minusWord[key][0].copy()
            minusWord[key][0]=tmpList[0].copy()
            
        
                
        #заполним размеры
        for key in minusWord:    
            tire = Tire()
            tire.brand='continental'
            tire.season='1' #1-зима 2-лето
            tire.get_razmer( minusWord[key][0])
            minusWord[key].append(tire)
            
        return minusWord   
    
    @staticmethod    
    def comp(templ_list=[],sour_list=[]):
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
    
    @staticmethod   
    def create_url(tire ):
        str_ret = '/podbor/'
        if tire.width  is None:
            str_ret += '0/'
        else:
            str_ret += str( tire.width) + '/'
        
        if tire.height  is None:
            str_ret += '0/'
        else:
            str_ret += str( tire.height) + '/'
            
        if tire.diameter  is None:
            str_ret += '0/'
        else:
            str_ret += str( tire.diameter) + '/'
        
        if tire.season  is None:
            str_ret += '0/0/'
        else:
            str_ret += str( tire.season) + '/0/'
            
        if tire.brand  is None:
            str_ret += '0'
        else:
            str_ret += str( tire.brand)     
        
        return str_ret
        

class Tire(object):
    def __init__(self):
        self._width = None 
        self.__height=None
        self.__diameter = None
        self.__brand = None 
        self.__season = None

    def get_brand(self):
        return self.__brand


    def get_season(self):
        return self.__season


    def set_brand(self, value):
        self.__brand = value


    def set_season(self, value):
        self.__season = value


    def del_brand(self):
        del self.__brand


    def del_season(self):
        del self.__season

        
        

    def get_diameter(self):
        return self.__diameter


    def set_diameter(self, value):
        self.__diameter = value


    def del_diameter(self):
        del self.__diameter
        
    diameter = property(get_diameter, set_diameter, del_diameter, "diameter's docstring")
        
    def get_height(self):
        return self.__height


    def set_height(self, value):
        self.__height = value
   
 

    def del_height(self):
        del self.__height

    height = property(get_height, set_height, del_height, "height's docstring")
   
   
     
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width = value
        
    @width.deleter
    def width(self):
        del self._width
    brand = property(get_brand, set_brand, del_brand, "brand's docstring")
    season = property(get_season, set_season, del_season, "season's docstring")
    
    def __str__(self):
        tmp_str = " " + self.__brand + " " + self._width + " " + self.__height +" " + self.__diameter  
        return tmp_str
        
    def get_razmer(self,list_w =[]):
        ''' разбирает список list
        если число от 12 до 22 - диаметр
                   от 30 до 90 - профиль
                   больше 100 - ширина
        '''
        if type(list_w) is not list:
            return False 
        
        for w in list_w:
            if w.isdigit():
                a = int(w)
                if a in range(12,24): self.__diameter=a
                if a in range(25,90): self.__height = a
                if a > 100:self._width=a
            else:
                if w[0]=='r':
                    w=w[1:]
                    if w.isdigit():
                        a = int(w)
                        self.__diameter=a