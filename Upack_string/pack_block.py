#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Замена строк внутри тех блоков типа {asdjer} и подобных
#   Версия:     2.0
#   Дата:       10.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

fileTranslated = 'TranslatedFileDialog.txt'
fileToTransl = 'outP.txt'
fileOriginal = 'Dialog.txt'
out_file_name = ""

from FilesOperation import readFile, writeFile
from Upack_string import block_util


if __name__ == '__main__':
    dataOriginal = readFile.read_file_rstrip(fileOriginal)
    dataTransl = readFile.read_file_rstrip(fileTranslated)
    dataToTransl = readFile.read_file_rstrip(fileToTransl)
    dataResult = []

    j = 0
    while j < len(dataToTransl):
        i = 0
        while i < len(dataOriginal):
            position = dataToTransl[j].find(dataOriginal[i])
            if (position > 0) and block_util.oxf_is_same_size(position, dataToTransl[j], dataOriginal[i]):
                if block_util.oxf_have_right_prefix(position, dataToTransl[j]):
                    dataToTransl[j] = dataToTransl[j].replace(dataOriginal[i], dataTransl[i])
            i += 1
        dataToTransl[j] += '\n'
        j += 1

    writeFile.write_list(out_file_name, dataToTransl)

# def readFileP(filename):
#     data = []
#     infile = open(filename, 'r', encoding='UTF8')
#     for line in infile:
#         line = line.replace('\r', '')
#         line = line.replace('\n', '')
#         data.append(line)
#     return data