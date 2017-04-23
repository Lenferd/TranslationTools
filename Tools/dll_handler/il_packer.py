#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  il unpacker
#   Назначение: запаковка il файлов
#   Версия:     1.0
#   Дата:       23.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os

from Modules.FilesOperation import readFile
from Modules.FilesOperation import find
from Modules.FilesOperation import writeFile

directory = "input_il"


if __name__ == '__main__':
    file_il = find.get_file_from_directory(directory)
    file_orig = find.get_file_from_directory("input_origin_il")
    file_transl = find.get_file_from_directory("input_translated_il")

    data = readFile.read_file_rstrip(file_il)

    data_orig = [[],[],[]]
    data_transl = [[],[],[]]

    infile = open(file_orig, 'r', encoding="UTF8")
    for line in infile:
        data_orig[0].append(line.strip().split('\t')[0])
        data_orig[1].append(line.strip().split('\t')[1])
        data_orig[2].append(line.strip().split('\t')[2])
    infile.close()

    infile = open(file_transl, 'r', encoding="UTF8")
    for line in infile:
        data_orig[0].append(line.strip().split('\t')[0])
        data_orig[1].append(line.strip().split('\t')[0])
        data_orig[2].append(line.strip().split('\t')[0])
    infile.close()

    for i in range(len(data)):
        index = data[i].find("ldstr")
        if index != -1:
            temp = line.split(' ')
            temp = [e for e in temp if e]
            if len(temp) > 3:
                temp = [temp[0], temp[1], ' '.join(temp[2:])]   # id, key, value
            if temp[0] in data_orig[0]:
                index = data_orig[0].index(temp[0])
                data[i].replace(data_orig[3][index], data_transl[3][index])

    outfile = open(os.path.join("result_il_bin", os.path.basename(file_il)), 'w', encoding="CP1251")
    for line in data:
        outfile.write(line + '\n')
    outfile.close()
