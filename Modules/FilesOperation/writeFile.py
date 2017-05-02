#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  write file
#   Назначение: Запись данных в файлы
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os

from Modules.FilesOperation import find as ffind

directory = "/result/"


def write_data(data_list, filename, *, prefix = ""):
    path = os.path.curdir + directory + prefix + '/'
    create_directory(path)

    outfile = open(path + filename + ".txt", 'w')
    for data in data_list:
        for line in data:
            outfile.write(line + '\n')
    outfile.close()


def write_data_with_filename(data_list, filename_list, filename, *, prefix=""):
    path = os.path.curdir + directory + prefix + '/'
    create_directory(path)

    outfile = open(path + filename + ".txt", 'w')
    for i in range(len(data_list)):
        outfile.write("'===" + ffind.find_directory_with_filename(filename_list[i]) + "===" + '\n')
        if len(data_list[i]) == 0:
            outfile.write("***EMPTY FILE***\n")
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


#   Запись с именами файлов игнорируя пустые блоки данных
def write_data_with_filename_wo_empty(data_list, filename_list, filename, *, prefix='', path=""):
    if path == "":
        path = os.path.curdir + directory + prefix + '/'
    else:
        path += prefix + '/'

    create_directory(path)

    outfile = open(path + filename + ".txt", 'w', encoding="UTF8")
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue
        outfile.write("'===" + ffind.find_directory_with_filename(filename_list[i]) + "===" + '\n')
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


"""   
    # Не знаю как назвать, выводится тип файлов и только один раз
    # Запись только в один файл?
    # Только для ОТСОРТИРОВАННЫХ
"""


def write_data_only_one_writted_type_sorted(data_list, filename_list_sorted, filename, *, path="", prefix="", postfix=""):
    if path == "":
        path = os.path.curdir + directory + prefix + '/' + postfix + '/'
    else:
        path += prefix + '/' + postfix + '/'

    create_directory(path)

    outfile = open(path + filename + ".txt", 'w', encoding="UTF8")

    global_ftype = ''
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue

        ftype = ffind.find_filetype(filename_list_sorted[i])
        if ftype != global_ftype:
            global_ftype = ftype
            outfile.write("'===" + global_ftype + "===" + '\n')
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


#   запиись во множество файлов. Каждый файл - для своего формата
def write_data_to_many_file_witch_sorting_ordering(data_list, filename_list_sorted, filename, *, path="", prefix="", postfix=""):
    if path == "":
        path = os.path.curdir + directory + prefix + '/' + postfix + '/'
    else:
        path += prefix + '/' + postfix + '/'
    create_directory(path)

    # outfile = open(path + filename + ".txt", 'w')
    global_ftype = ''
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue

        ftype = ffind.find_filetype(filename_list_sorted[i])
        if ftype != global_ftype:
            global_ftype = ftype
            outfile = open(path + filename + "_" + global_ftype + ".txt", 'w', encoding="UTF8")
        for line in data_list[i]:
            outfile.write(line + '\n')
    try:
        outfile.close()
    except UnboundLocalError:
        print(filename + " is empty")


def write_list_without_adding_newline(data, filename, *, prefix="", postfix=""):
    path = os.path.curdir + directory + prefix + '/' + postfix + '/'
    create_directory(path)

    outfile = open(path + filename + ".txt", 'w', encoding="UTF8")
    for line in data:
        outfile.write(line)
    outfile.close()


def write_list(data, filename, *, prefix="", postfix="", path=""):
    if path == "":
        path = os.path.curdir + directory + prefix + '/' + postfix + '/'
    else:
        path = os.path.join(path, prefix, postfix)
        # path += prefix + '/' + postfix + '/'
    create_directory(path)

    outfile = open(os.path.join(path, filename) + ".txt", 'w', encoding="UTF8")
    for line in data:
        outfile.write(line + '\n')
    outfile.close()


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

