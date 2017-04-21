#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Замена строк внутри тех блоков типа {asdjer} и подобных
#   Версия:     2.0
#   Дата:       10.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

from FilesOperation import readFile, writeFile
from Upack_string import block_util

fileTranslated = r'.\input\translated_dialog.txt'
fileToTransl = r'.\input\all_quo_orig_block.txt'
fileOriginal = r'.\input\result_dialog.txt'

out_file_name = "translate_in_block_dialog"

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
        j += 1

    writeFile.write_list(dataToTransl, out_file_name)