#  Copyright 2016 Shumihin Sergey

import os 
import sys

if len(sys.argv) == 1:
    print("Ошибка выполнения команды. Воспользуйтесь справкой -h.")
    sys.exit()

if sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
    print("usage: <directory> [options]")
    print("\nOptions and arguments:")
    print("-s\t: Удаление файлов с системными строками")
    print("--*\t: Оставить только файлы с минусом в разрешении")
    print("-c [arg] -e\t: Оставить файлы с указанным разрешением (-e закрывает список разрешений)")
    print("\n Пример: .\Dir -s --*")
    sys.exit()
elif sys.argv[1].find('\\'):
    path = sys.argv[1]
else:
    print("Ошибка выполнения команды. Воспользуйтесь справкой -h.")

def delSystemFile():
    filesList = []
    for root, dirs, files in os.walk(path):
        for name in files:
            filesList.append(os.path.join(root, name))

    for file in filesList:
        infile = open(file, 'rb')

        data = bytearray(b'')
        for x in infile:
            data = data + x

        sysstr1 = bytearray(b'\x4E\x6F\x72\x6D\x61\x6C\x00\x00\x0B\x00\x00\x00\x48\x69\x67\x68\x6C\x69\x67\x68\x74\x65\x64')
        sysstr2 = bytearray(b'\x48\x6F\x72\x69\x7A\x6F\x6E\x74\x61\x6C\x00\x00\x08\x00\x00\x00\x56\x65\x72\x74\x69\x63\x61\x6C')


        if data.find(sysstr1) > 0 or data.find(sysstr2) > 0:
            print("File :" + str(file) + " deleted")
            infile.close()
            os.remove(file)
        else:
            infile.close()

def delAllWithoutMin():
    filesList = []
    for root, dirs, files in os.walk(path):
        for name in files:
            filesList.append(os.path.join(root, name))

    for file in filesList:
        tempstr = file.split('.')
        if tempstr[len(tempstr)-1].find('-') == -1:
            print("File :" + str(file) + " deleted")
            os.remove(file)

def delButNotThis(notDel):
    filesList = []
    for root, dirs, files in os.walk(path):
        for name in files:
            filesList.append(os.path.join(root, name))
    i = 0
    while i < len(filesList):
        tempstr = filesList[i].split('.')
        for templ in notDel:
            if tempstr[len(tempstr)-1] == templ:
                filesList.pop(i)
        i+=1

    for file in filesList:
        print("File :" + str(file) + " deleted")
        os.remove(file)



if (len(sys.argv) < 3):
    print("Где аргумент то, алло!")
    sys.exit()

i = 2
while (sys.argv[i]):
    if sys.argv[i] == '-s':
        delSystemFile()
    elif sys.argv[i] == '--*':
        delAllWithoutMin()
    elif sys.argv[i] == '-c':
        if (len(sys.argv) < 1+i+1):
            print("А имена файлов то где?")
            sys.exit()
        i+=1
        kingFiles = []
        while sys.argv[i] != '-e':
            kingFiles.append(sys.argv[i])
            if (len(sys.argv) < 1+i+1):
                print("Не закрыт список расширений")
                sys.exit()
            i+=1
        delButNotThis(kingFiles)



    if (len(sys.argv) > 1 + i):
        i+=1
    else:
        break
