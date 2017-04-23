#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Извлечение строк внутри тех блоков типа {asdjer} и подобных
#   Версия:     1.0
#   Дата:       10.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

files_directory = r'./input'

from Modules.TextOperations import encoding_fix

from Modules.FilesOperation import readFile, writeFile, find
from Modules.TextOperations import text_filter
from Tools.Block_handler import block_util

if __name__ == '__main__':

    list_of_files = []

    list_of_files = find.construct_file_three(files_directory)

    for file in list_of_files:
        resultData = []
        file_data = readFile.read_file_rstrip(file)
        for line in file_data:
            resultData += block_util.oxf_search_string(line)

        for i in range(len(list_of_files)):
            k = 0
            while k < len(resultData):
                if resultData[k] == '\n' or resultData[k] == " \n":
                    resultData.pop(k)
                    k -= 1
                k += 1

        resultData = encoding_fix.fix_codign_list(resultData)
        resultData, removed = text_filter.filter_text(resultData)

        writeFile.write_list_without_adding_newline(resultData, find.find_filename(file), prefix="out")
        writeFile.write_list_without_adding_newline(removed, find.find_filename(file), prefix="out_removed")
