#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  Oxenfree Packer
#   Назначение: Запихиваем всё это дерьмо обратно
#   Версия:     2.0
#   Дата:       10.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

from Modules.BinaryParser import binary_filler
from Modules.FilesOperation import readFile, find

original_file = "input/original.txt"
translated_file = "input/translate.txt"

path = "/mnt/sda3/TT/TT_OF4/Unity_Assets_Files/resources"
outpath = "./result_hex"

if __name__ == '__main__':
    original_data = readFile.read_file_rstrip(original_file)
    translated_data = readFile.read_file_rstrip(translated_file)

    binary_file_list = find.construct_file_three(path)

    bin_original_data = binary_filler.convert_text_to_binary(original_data)
    bin_transl_data = binary_filler.convert_text_to_binary(translated_data)
    binary_filler.parse_and_fill_binary_list(binary_file_list,
                                             bin_original_data, bin_transl_data, binary_file_list, outpath)
