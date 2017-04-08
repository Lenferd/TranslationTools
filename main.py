#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
# from BinaryParser import binaryReaderLib as binaryParser
from BinaryParser import readFile as freader

filepatch = "./examples"

if __name__ == "__main__":
    # Construct list of files
    # TODO можно добавить возможность указывать маску, по которой будут искаться файлы (т.е. разрешение)
    fileList = freader.construct_file_three(filepatch)


    print(list)