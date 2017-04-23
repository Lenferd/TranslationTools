#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  il unpacker
#   Назначение: Распаковка il файлов
#   Версия:     1.0
#   Дата:       23.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


import sys
import os

sys.path.insert(0, os.path.join("..", ".."))
from Modules.FilesOperation import readFile
from Modules.FilesOperation import find

directory = "input_il"

if __name__ == '__main__':
    file = find.get_file_from_directory(directory)

    file = open(file, 'r', encoding="CP1251")
    data = [s.rstrip() for s in file.readlines()]

    result_data = []
    for line in data:
        index = line.find("ldstr")
        if index != -1:
            temp = line.split(' ')
            temp = [e for e in temp if e]
            if len(temp) > 3:
                temp = [temp[0], temp[1], ' '.join(temp[2:])]
                print(temp)
            result_data.append(temp)

    outfile = open(os.path.join(".", "result_il", os.path.basename(file) + ".txt"), 'w', encoding="UTF8")

    for i in range(len(result_data)):
        outfile.write(str(result_data[i][0]) + "\t" + str(result_data[i][1]) + "\t" + str(result_data[i][2]) + '\n')
    # writeFile.write_list(result_data, os.path.basename(file), path=os.path.join('.', "result_il"))

