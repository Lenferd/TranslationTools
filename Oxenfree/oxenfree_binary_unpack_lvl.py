#!/usr/bin/python3
# -*- coding: utf-8 -*-
#   Программа:  OxenfreeUnpacker
#   Назначение: Вытаскиваем текст из файлов
#   Версия:     3.1
#   Дата:       8.04.17
#   Модифик:    21.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import sys
sys.path.insert(0, os.path.pardir)

from Modules.BinaryParser import binary_parser as bparser
from Modules.FilesOperation import find as ffind
from Modules.FilesOperation import readFile as freader
from Modules.FilesOperation import writeFile as fwriter
from Modules.TextOperations import text_filter

# filepatch = "/mnt/sda3/TT/TT_OF4/test"
# filepatch = r"D:\TT\TT_OF4\LVL_COPIED2"
# filepatch = "./examples"
dir_path = r"../Oxenfree_data/test2"
dir_lvl = r"../Oxenfree_data/test2/input_lvl"

#   out path
prefix_lvl = "result_lvl"     # folder in the result
prefix_dialog = "result_dialogs"     # folder in the result
postfix = "fileinfo"        # underfolder in the prefix folder (for file info)

if __name__ == "__main__":
    """ Block 0 """
    if len(sys.argv) < 2:
        pass
    else:
        dir_path = sys.argv[1]
        dir_lvl = sys.argv[1] + "/input_lvl"

    # Construct list of files (full route)
    file_list = ffind.construct_file_three(dir_lvl, ignoring_directories=["resources"])

    # get all file data
    binary_data = freader.read_binary_files(file_list)

    # get strings
    strings = bparser.parse_binary_list(binary_data)
    # now we can use filtres
    result_quo, result, removed = text_filter.oxenfree_filter_lvl(strings, start_str=r"\{\"_id.*")

    # ordering
    result_quo, ordering_result_quo = text_filter.ordering_by_filetype(result_quo, file_list)
    result, ordering_result = text_filter.ordering_by_filetype(result, file_list)
    removed, ordering_removed = text_filter.ordering_by_filetype(removed, file_list)

    # print data
    fwriter.write_data_only_one_writted_type_sorted(result_quo, ordering_result_quo, "result_quo_all",
                                                    prefix=prefix_dialog, path=dir_path)
    fwriter.write_data_to_many_file_witch_sorting_ordering(result_quo, ordering_result_quo, "result_quo",
                                                           prefix=prefix_dialog, path=dir_path)

    fwriter.write_data_only_one_writted_type_sorted(result, ordering_result, "lvl_result_all",
                                                    prefix=prefix_lvl, path=dir_path)
    fwriter.write_data_to_many_file_witch_sorting_ordering(result, ordering_result, "lvl_result",
                                                           prefix=prefix_lvl, path=dir_path)
    #
    fwriter.write_data_with_filename_wo_empty(removed, ordering_removed, "removed",
                                              prefix=postfix, path=dir_path)

    # print filetype
    fwriter.write_list(ffind.find_all_type(ordering_result), "filetype",
                       postfix=postfix, path=dir_path)
    fwriter.write_list(ffind.find_all_type(ordering_removed), "filetype_rem",
                       postfix=postfix, path=dir_path)

    empty_files_list = ffind.find_empty_files(result, ordering_result)
    fwriter.write_list(empty_files_list, 'emptyRes',
                       postfix=postfix, path=dir_path)

    empty_files_list = ffind.find_empty_files(result_quo, ordering_result_quo)
    fwriter.write_list(empty_files_list, 'emptyQuo',
                       postfix=postfix, path=dir_path)
