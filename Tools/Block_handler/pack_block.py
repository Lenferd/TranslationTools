#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Замена строк внутри тех блоков типа {asdjer} и подобных
#   Версия:     2.1
#   Дата:       10.04.17
#   Мод:        23.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import sys
import os

sys.path.insert(0, os.path.join(".."))

from Modules.FilesOperation import readFile, writeFile
from Tools.Block_handler import block_util
from Modules.TextOperations import encoding_fix

fileTranslated = r'.\input\translated_dialog.txt'
fileToTransl = r'.\input\all_quo_orig_block.txt'
fileOriginal = r'.\input\result_dialog.txt'

out_file_name = r".\translate_in_block_dialog"

if __name__ == '__main__':
    if len(sys.argv) < 4:
        pass
    else:
        fileToTransl = sys.argv[1]
        fileOriginal = sys.argv[2]
        fileTranslated = sys.argv[3]
        out_file_name = sys.argv[4]

    dataOriginal = readFile.read_file_rstrip(fileOriginal)
    dataTransl = readFile.read_file_rstrip(fileTranslated)
    dataToTransl = readFile.read_file_rstrip(fileToTransl)
    dataResult = []

    dataOriginal = encoding_fix.revert_fix_coding(dataOriginal)
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

    writeFile.write_list(dataToTransl, os.path.basename(out_file_name).split(".")[0], path=os.path.dirname(out_file_name))
