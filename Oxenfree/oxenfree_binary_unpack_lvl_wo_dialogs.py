#!/usr/bin/python3
# -*- coding: utf-8 -*-
#   Программа:  OxenfreeUnpacker
#   Назначение: Вытаскиваем текст из файлов
#   Версия:     3.0
#   Дата:       8.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

# from BinaryParser import binaryReaderLib as binaryParser
from Modules.BinaryParser import binary_parser as bparser
from Modules.FilesOperation import find as ffind
from Modules.FilesOperation import readFile as freader
from Modules.FilesOperation import writeFile as fwriter
from Modules.TextOperations import text_filter

# filepatch = "/mnt/sda3/TT/TT_OF4/test"
filepatch = "/mnt/sda3/TT/TT_OF4/Lvl"
# filepatch = "./examples"

#   out path
prefix = "lvl_to_transl4_wo_dialogs"     # folder in the result
postfix = "fileinfo"        # underfolder in the prefix folder (for file info)

if __name__ == "__main__":
    file_list = ffind.construct_file_three(filepatch)

    # get all file data
    binary_data = freader.read_binary_files(file_list)

    # get strings
    strings = bparser.parse_binary_list(binary_data)

    # now we can use filtres
    result, removed = text_filter.oxenfree_filter_resources(strings)

    # ordering
    result, ordering_result = text_filter.ordering_by_filetype(result, file_list)
    removed, ordering_removed = text_filter.ordering_by_filetype(removed, file_list)

    fwriter.write_data_only_one_writted_type_sorted(result, ordering_result, "result_all", prefix=prefix)
    fwriter.write_data_to_many_file_witch_sorting_ordering(result, ordering_result, "result", prefix=prefix)
    fwriter.write_data_with_filename_wo_empty(removed, ordering_removed, "removed", prefix=prefix)

    # print filetype
    fwriter.write_list(ffind.find_all_type(ordering_result), "filetype", prefix=prefix, postfix=postfix)

    empty_files_list = ffind.find_empty_files(result, ordering_result)
    fwriter.write_list(empty_files_list, 'empty', prefix=prefix, postfix=postfix)

