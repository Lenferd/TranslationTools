#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  retranslate files
#   Назначение: Перенос перевода
#   Версия:     2.1
#   Дата:       9.04.17
#   Мод:        22.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import sys
import os
import copy
sys.path.insert(0, os.path.join("..", ".."))

from Modules.FilesOperation import readFile, writeFile
from Modules.TextOperations.find_text import is_have_russian_symbols

# print(os.path.pardir)

def_data_fold = r"Retranslate_data"
def_dir = os.path.join("Retranslate_data", "example")


# file_original = 'Orig/orig.txt'
# file_translated = 'Transl/transl.txt'
# file_new = 'toTransl/lvl_text_result_all.txt'
# prefix = "lvl_text"


def find_text(_original_data, _translated_data, _originalNew_data, copyOriginal=0):
    result_data = []
    original_data = copy.copy(_original_data)
    translated_data = copy.copy(_translated_data)
    originalNew_data = _originalNew_data
    for line in originalNew_data:
        i = 0
        while i < len(original_data):
            if line == original_data[i]:
                if is_have_russian_symbols(translated_data[i]):
                    result_data.append(translated_data.pop(i))
                    original_data.pop(i)
                else:
                    if copyOriginal:
                        result_data.append(line)
                    else:
                        result_data.append("")
                    translated_data.pop(i)
                    original_data.pop(i)
                break
            elif i + 1 == len(original_data):
                if copyOriginal:
                    result_data.append(line)
                else:
                    result_data.append("")
            i += 1

    return result_data, original_data, translated_data


if __name__ == '__main__':

    if len(sys.argv) < 2:
        dir_with_data = def_dir
    else:
        dir_with_data = os.path.join(def_data_fold, sys.argv[1])

    # input_original_text
    # input_translated_text
    # input_file_to_translate
    # result_translated

    file_original = os.path.join(dir_with_data, "input_original_text")  # , filename + ".txt")
    file_translated = os.path.join(dir_with_data, "input_translated_text")  # ", filename + ".txt")
    file_new = os.path.join(dir_with_data, "input_file_to_translate")  # , filename + ".txt")

    if len(os.listdir(file_original)) != 1 and len(os.listdir(file_translated)) != 1 and len(os.listdir(file_new)) != 1:
        print("In folder ", file_original, ", ", file_translated, ", ", file_new, "  not a one file")
        exit(-1)

    file_original = os.path.join(dir_with_data, "input_original_text", os.listdir(file_original)[0])
    file_translated = os.path.join(dir_with_data, "input_translated_text", os.listdir(file_translated)[0])
    file_new = os.path.join(dir_with_data, "input_file_to_translate", os.listdir(file_new)[0])

    if file_original.find(".txt") == -1 or file_translated.find(".txt") == -1 or file_new.find(".txt") == -1:
        print("Files should be in txt format!")
        exit(-2)

    original_text = readFile.read_file_rstrip(file_original)
    translated_text = readFile.read_file_rstrip(file_translated)
    originalNew_text = readFile.read_file_rstrip(file_new)

    translated_data, original_data_old, translated_data_old = \
        find_text(original_text, translated_text, originalNew_text)

    translated_data_with_orig, temp1, temp2 = \
        find_text(original_text, translated_text, originalNew_text, 1)

    output_path = os.path.join(dir_with_data, "result_translated")
    writeFile.write_list(translated_data, os.path.basename(file_new).split(".")[0] + "_wo_originals", path=output_path)
    writeFile.write_list(translated_data_with_orig, os.path.basename(file_new).split(".")[0], path=output_path)
    writeFile.write_list(original_data_old, "origNotFound", path=output_path)
    writeFile.write_list(translated_data_old, "translNotFound", path=output_path)
