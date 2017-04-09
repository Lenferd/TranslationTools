# -*- coding: utf-8 -*-
#   Программа:  OxenFreeUnpacker
#   Назначение: Вытаскиваем текст из файлов
#   Версия:     1.0
#   Автор:      Lenferd (DeysonSH@gmail.com)

"""     Принцип работы:
        1. Открываем бинарный файл
        2. Склеиваем всё в одну строчку?
        3. Идём по строке, и ищем точку отсчёта
"""


"""     Возможные проблемы, которые хуй знает как решать
        1. Не ебу, что там с кодировками
    Кодировка наверняка ISO-8859-1
"""

#      Статичные параметры
#   Папка с данными
filePatch = r"D:\TT\TT_OF3_Tools\_UNPACKERS_new"

import os

#       БЛОК ФУНКЦИЙ 

def findDir(string):
    buf = string[:string.rfind("\\")]
    buf = buf[buf.rfind("\\")+1:]
    return buf
    
def isSize(data, i):
    result = False
    if ((i % 4 == 0) and (i+4 < len(data))): 
    # условие не выхода за пределы и соответствие блоку размерности
        if (data[i] > 0 and data[i+1] >= 0) or (data[i] >= 0 and data[i+1] > 0):    
        # первый может быть равен нулю, если второго достаточно        
            if (data[i+3] == 0) and (data[i+2] == 0) and (data[i] + data[i+1] * 256 < len(data)): 
            # не выходит ли фраза за пределы байтовой строки
                result = True
    return result

def isNormalString(data, i):
    #На вход получаем индекс i (в дата под этим индексом длина строки)
    #size = data[i] + 256 * data[i+1] хз зачем
    k = i+4
    #Хорошо бы сделать проверку на системные символы
    if (data[k] > 31) and (data[k+1] > 31): 
    # Первые два проверяем на диапазон. На 128 не ограничишь, ибо всё к хуям летит из-за трёхбайтовых кавычек и многоточий
        return True
    else:
        return False


def ReadString(data, i):
    size = data[i] + 256 * data[i+1]      #Размер нашей строки
    i=i+4               #Выполняем смещение на начало текста
    resultstring = ''
    bytedata = bytearray(b'')
    j = 0
    while (j < size):
        if data[i] == 0:
            return('NULL')
        if data[i] == 10:
            bytedata.append(92)
            bytedata.append(110)
        elif data[i] == 13:
            bytedata.append(92)
            bytedata.append(114)
        else:
            bytedata.append(data[i])
        j+=1
        i+=1
    resultstring = bytedata.decode('ISO-8859-1')
    return resultstring

#       ПРОГРАММА

#результат
stringData = []

#Находим файлы, из которых необходимо вытащить текст
dirsList = os.listdir(path=filePatch)

for directory in dirsList:
    for root, dirs, files in os.walk(filePatch+'\\' + directory):
        for name in files:
            filename = os.path.join(root, name)
            infile = open(filename, 'rb')
            data = bytearray(b'')
            #Получаем целую байтовую строку
            for x in infile:
                data = data + x 
            #Следующим шагом необходимо найти в этой чёртовой строке человеческие буквы
            i = 0
            while (i < len(data)):  #data - байтовая строка (bytearray)
                if (isSize(data, i) and (isNormalString(data, i))): #проверка, является ли данный блок числом-размером строки и есть ли в строке человеческие буквы
                    string = ReadString(data, i) + '\n' #Лишний символ же приматываем, поэтому в i+= на 1 меньше
                    i += len(string) + 1 #перепрыгиваем строку
                    if (len(string) > 1):                   #На случай, если придётся переделать NormalizeString
                        stringData.append(string) #Дополнительно приводим строку в нормальный вид
                else:
                    i+=1

    outfile = open("filestr\\"+ directory + '.txt', 'w', encoding = 'ISO-8859-1')
    outfile.writelines(stringData)
    stringData = []