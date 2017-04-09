#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from BinaryParser import binaryReaderLib as binaryParser
from BinaryParser import binary_parser as bparser
from FilesOperation import readFile as freader
from FilesOperation import writeFile as fwriter
from TextFiltres import text_filter

filepatch = "./examples/only2.2"

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

    # fwriter.write_data(result, "result")
    fwriter.write_data_with_filename(result, file_list, "result")
    # fwriter.write_data(removed, "removed")
    fwriter.write_data_with_filename(removed, file_list, "removed")

    empty_files_list = fwriter.find_empty_files(result, file_list)
    fwriter.write_list(empty_files_list, 'empty')
