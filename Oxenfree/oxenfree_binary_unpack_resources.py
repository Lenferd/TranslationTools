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

import sys

# file_patch = "/mnt/sda3/TT/TT_OF4/Unity_Assets_Files/resources"
# filepatch = "/mnt/sda3/TT/TT_OF4/test"
dir_patch = "../Oxenfree_data/test2"
file_resources = "../Oxenfree_data/test2/input_resources"
# filepatch = "./examples"

#   out path
prefix = "result_resources"     # folder in the result
postfix = "fileinfo"        # underfolder in the prefix folder (for file info)

if __name__ == "__main__":
    """ Block 0 """
    if len(sys.argv) < 2:
        pass
    else:
        dir_patch = sys.argv[1]
        file_resources = sys.argv[1] + "/input_resources"

    """ Block 1 open & read
        На выходе получаем list из листов соответствующих поданных на вход файлов (file_list)
        + данные внутри преобразованы в UTF8 из бинарного вида
    """
    # Construct list of files (full route)
    # TODO можно добавить возможность указывать маску, по которой будут искаться файлы (т.е. разрешение)
    file_list = ffind.construct_file_three(file_resources)

    # get all file data
    binary_data = freader.read_binary_files(file_list)

    # get strings
    strings = bparser.parse_binary_list(binary_data)

    """ Block 2
        Использование фильтра для отсеивания лишних строг (грубая обработка)
        Фильтр настраивается
    """
    # now we can use filtres
    result, removed = text_filter.oxenfree_filter_resources(strings)

    """ Block 3
        Упорядочивание массивов данных по типу файлов
    """
    # ordering
    result, ordering_result = text_filter.ordering_by_filetype(result, file_list)
    removed, ordering_removed = text_filter.ordering_by_filetype(removed, file_list)

    fwriter.write_data_only_one_writted_type_sorted(result, ordering_result, "result_all",
                                                    prefix=prefix, path=dir_patch)
    fwriter.write_data_to_many_file_witch_sorting_ordering(result, ordering_result, "result",
                                                           prefix=prefix, path=dir_patch)

    fwriter.write_data_with_filename_wo_empty(removed, ordering_removed, "removed",
                                              prefix=prefix, path=dir_patch)

    # print filetype
    fwriter.write_list(ffind.find_all_type(ordering_result), "filetype",
                       prefix=prefix, postfix=postfix, path=dir_patch)

    empty_files_list = ffind.find_empty_files(result, ordering_result)
    fwriter.write_list(empty_files_list, 'empty',
                       prefix=prefix, postfix=postfix, path=dir_patch)
