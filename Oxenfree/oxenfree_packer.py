# Назначение: запаковка субтитров
# Древняя версия: Ты должен был уничтожить это зло, а не пользоваться им!
Debug = 1

import os
import sys

#      Данные
#   Имя файла с переведёнными строками
translated_file = r'.\input\translated_lvl_text.txt'
#   Имя файла с оригинальными строками
original_file = r'.\input\lvl_text_result_all.txt'
#   Директория для обработки
files_directory = r'.\lvl'
#filesDirectory = r'D:\Games\Oxenfree\Oxenfree_Data\Unity_Assets_Files\resources'


#   Считывание данных из файла по заданному пути
def readFile(filename):
    data = []
    infile = open(filename, 'r', encoding='UTF8')
    for line in infile:
        line = line.rstrip().replace('\\r', '\r').replace('\\n', "\n")    #Урезается конец файла
        data.append(line)
    return data

#   Высчитываем, сколько нужно добавить пробелов к строке
def SpaceSize(origstring, translstring):
    size = (len(origstring) % 4) - (len(translstring) % 4)
    if (size < 0):
        size+=4
    return size

def replaceHex(data, original, transl):
    position = data.find(b'\x00' + original) + 1
    resultdata = data[0:position]
    resultdata += transl
    resultdata += data[position+len(original):]
    return resultdata

def isSize(data, i):
    if ((i % 4 == 0) 
        and (i+4 < len(data)) 
        and (data[i] >= 0) 
        and (data[i+1] >= 0) 
        and (data[i+2] == 0)
        and (data[i+3] == 0)
        and (data[i] + data[i+1] * 256 < len(data))): #не выходит ли фраза за пределы байтовой строки
        return True
    else :
        return False 

def dontHaveSymbol(str):
    for char in str:
        if (char > 32): #Пробел не включаем
            return False
    return True

def isEqualityString(position, data, orig):
    if (isSize(data, position - 4)):
        stringsize = data[position-4] + 256*(data[position-3])
        if (Debug == 2):
            print(orig)
            print(len(orig))
            print(stringsize)
        if orig == data[position:position + stringsize]:
            return True
        if len(orig) > stringsize:
            return False
        if stringsize - len(orig) <= 5:
            if (Debug == 2):
                print(data[position + len(orig):position+stringsize])
            if dontHaveSymbol(data[position + len(orig):position+stringsize]):
                if (orig == data[position:position+len(orig)]):
                    return True
    return False

def havespaceafter(data, position, origstring):
    origsize = len(origstring)
    size = data[position] + 256 * data[position + 1] 
    return size - origsize

if __name__ == '__main__':

    result_dir = ""
    if len(sys.argv) < 4:
        pass
    else:
        files_directory = sys.argv[1]
        original_file = sys.argv[2]
        translated_file = sys.argv[3]
        if len(sys.argv) == 5:
            result_dir = os.path.normpath(sys.argv[4])

    # список файлов
    listOfFiles = []
    dataOriginal = readFile(original_file)
    dataTranslated = readFile(translated_file)
    dataByteOriginal = []
    dataByteTranslated = []

    #Сразу преобразуем строки из Original в битовое представление
    for line in dataOriginal:
        dataByteOriginal.append(bytearray(line, encoding = 'UTF8'))

    #И то же самое для Translated
    for line in dataTranslated:
        dataByteTranslated.append(bytearray(line, encoding = 'UTF8'))

    #Заполняем список файлов
    for root, dirs, files in os.walk(files_directory):
        for name in files:
            filename = os.path.join(root, name)
            listOfFiles.append(filename)


    #открываем файлы и работаем с ними
    for filename in listOfFiles:
        #print(filename)
        infile = open(filename, 'rb')
        data = bytearray(b'')
        for x in infile:
            data = data + x

        #получили битовую строку из файла
        #теперь в этой строке нужно найти нашу оригинальную строку
        position = 0
        i = 0
        while (i < len(dataByteOriginal)):
            position = data.find(b'\x00' + dataByteOriginal[i])
            if (Debug == 2):
                print(dataByteOriginal[i])
                print(position)
            if ((position != -1)):                        #Если у нас находится оригинальная строка среди всей битовой строки, проверяем, всю ли строку мы берём
                position +=1    # чиним т.к. ищем с \x00
                if (isEqualityString(position, data, dataByteOriginal[i])):                         #Проверяем совпадение по длине
                    tempPlusString = b' ' * SpaceSize(dataByteOriginal[i], dataByteTranslated[i])   #Сколько добавляем пробелов из-за добавления ру строки
                    dataByteTranslated[i] += tempPlusString                                         #К нашей результирующей строке перевода добавляем пробелы
                    #print(dataB#yteTranslated[i])
                    diff = havespaceafter(data, position - 4, dataByteOriginal[i])                  #Высчитываем разницу в символов (для изменения размера строки)
                    data = replaceHex(data, dataByteOriginal[i], dataByteTranslated[i])             #Заменяем строчку
                    #теперь нужно ещё поменять размер
                    position -= 4                               #прыгаем на первую ячейку с числом
                    size = len(dataByteTranslated[i]) + diff
                    if (size >= 256):
                        size2 = size // 256
                        size = size - 256*size2
                        data[position] = size
                        data[position+1] = size2
                    else:
                        data[position] = size
            i+=1
            #else:
                #i+=1                                            #переходим на след элемент, если только проверили возможные повторы

        if result_dir == "":
            outfile = open(filename, 'wb')
        else:
            # print(filename.split(files_directory))
            # print(result_dir)
            kek = os.path.normpath(filename.split(files_directory)[-1]);
            out_direcories = result_dir + kek
            try:
                os.makedirs(os.path.dirname(out_direcories))
            except FileExistsError:
                pass
                # print("Directory already exist")
            # print(result_dir)
            # print(kek)
            # print(os.path.join(result_dir, kek))

            # print(os.path.join(result_dir, kek))
            # print(os.path.join(result_dir, filename.split(files_directory)[-1]))
            outfile = open(out_direcories, 'wb')

        outfile.write(data)
        outfile.close()