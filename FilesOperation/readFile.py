#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  readFile
#   Назначение: Считывание бинарных данных из файла
#   Версия:     2.0
#   Дата:       8.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)
import os


def read_binary_file(filename):
    infile = open(filename, 'rb')
    data = bytearray(b'')
    # get all bytestring
    for x in infile:
        data = data + x
    return data


def read_binary_files(files_list):
    binary_data = []

    for filename in files_list:
        infile = open(filename, 'rb')
        data = bytearray(b'')
        # get all bytestring
        for x in infile:
            data = data + x
        binary_data.append(data)

    return binary_data


def construct_file_three(path):
    files_list = []
    # first - find files in root dir
    for root, dirs, files in os.walk(path):
        for name in files:
            files_list.append(os.path.join(root, name))

    dirs_list = os.listdir(path=path)

    for directory in dirs_list:
        for root, dirs, files in os.walk(path + '\\' + directory):
            for name in files:
                files_list.append(os.path.join(root, name))

    return files_list

