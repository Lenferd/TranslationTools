#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  retranslate files
#   Назначение: Перенос перевода
#   Версия:     2.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

file_original = 'Orig/orig.txt'
file_translated = 'Transl/transl.txt'
file_new = 'toTransl/lvl_text_result_all.txt'
prefix = "lvl_text"

from Modules.FilesOperation import readFile, writeFile
from Modules.TextOperations.find_text import is_have_russian_symbols


def find_text(original_data, translated_data, originalNew_data):
    result_data = []

    for line in originalNew_data:
        i = 0
        while i < len(original_data):
            if line == original_data[i]:
                if is_have_russian_symbols(translated_data[i]):
                    result_data.append(translated_data.pop(i))
                    original_data.pop(i)
                else:
                    result_data.append("")
                    translated_data.pop(i)
                    original_data.pop(i)
                break
            elif i + 1 == len(original_data):
                result_data.append("")
            i += 1

    return result_data, original_data, translated_data


if __name__ == '__main__':
    original_text = readFile.read_file_rstrip(file_original)
    translated_text = readFile.read_file_rstrip(file_translated)
    originalNew_text = readFile.read_file_rstrip(file_new)

    translated_data, original_data_old, translated_data_old =\
        find_text(original_text, translated_text, originalNew_text)

    writeFile.write_list(translated_data, "toSite", prefix=prefix)
    writeFile.write_list(original_data_old, "origNotFound", prefix=prefix)
    writeFile.write_list(translated_data_old, "translNotFound", prefix=prefix)