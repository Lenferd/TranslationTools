#!/usr/bin/python3
# -*- coding: utf-8 -*-
#   Программа:  OxenfreeUnpacker
#   Назначение: Вытаскиваем текст из файлов
#   Версия:     3.0
#   Дата:       8.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

# from BinaryParser import binaryReaderLib as binaryParser
from BinaryParser import binary_parser as bparser
from FilesOperation import readFile as freader
from FilesOperation import writeFile as fwriter
from TextFiltres import text_filter
from FilesOperation import find as ffind

filepatch = "/mnt/sda3/TT/TT_OF4/Unity_Assets_Files"
# filepatch = "./examples"

if __name__ == "__main__":
    # Construct list of files (full route)
    # TODO можно добавить возможность указывать маску, по которой будут искаться файлы (т.е. разрешение)
    file_list = freader.construct_file_three(filepatch)

    # get all file data
    binary_data = freader.read_binary_files(file_list)

    # get strings
    strings = bparser.parse_binary_list(binary_data)

    # now we can use filtres
    result, removed = text_filter.oxenfree_filter(strings)

    # ordering
    result, ordering_result = text_filter.ordering_by_filetype(result, file_list)

    # fwriter.write_data(result, "result")
    fwriter.write_data_with_filename(result, ordering_result, "result")
    # fwriter.write_data(removed, "removed")
    # fwriter.write_data_with_filename_wo_empty(removed, file_list, "removed")

    empty_files_list = ffind.find_empty_files(result, ordering_result)
    fwriter.write_list(empty_files_list, 'empty')
