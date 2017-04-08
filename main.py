#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
# from BinaryParser import binaryReaderLib as binaryParser
from BinaryParser import readFile as freader
from BinaryParser import binary_parser as bparser
from TextFiltres import text_filter

filepatch = "./examples"

if __name__ == "__main__":
    # Construct list of files (full route)
    # TODO можно добавить возможность указывать маску, по которой будут искаться файлы (т.е. разрешение)
    file_list = freader.construct_file_three(filepatch)

    # get all file data
    binary_data = freader.read_binary_files(file_list)

    # get strings
    strings = bparser.parse_binary_list(binary_data)

    result, removed = text_filter.oxenfree_filter(strings)


    # now we can use filtres
    print(result)
    print(removed)
    for data in result:
        for line in data:
            print(line)
