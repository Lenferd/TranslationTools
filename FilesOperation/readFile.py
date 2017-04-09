#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  readFile
#   Назначение: Считывание бинарных данных из файла
#   Версия:     2.0
#   Дата:       8.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


def read_binary_file(filename):
    infile = open(filename, 'rb')
    data = bytearray(b'')
    # get all bytestring
    for x in infile:
        data = data + x
    infile.close()
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
        infile.close()

    return binary_data


def read_file_rstrip(filename):
    file = open(filename, 'r', encoding="UTF8")
    data = [s.rstrip() for s in file.readlines()]
    file.close()
    return data
