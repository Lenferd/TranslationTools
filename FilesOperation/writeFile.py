#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  write file
#   Назначение: Запись данных в файлы
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import FilesOperation.find as ffind

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
        outfile.write("===" + ffind.find_directory_with_filename(filename_list[i]) + "===" + '\n')
        if len(data_list[i]) == 0:
            outfile.write("***EMPTY FILE***\n")
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


def write_data_with_filename_wo_empty(data_list, filename_list, filename, *, prefix=''):
    path = os.path.curdir + directory + prefix + '/'
    create_directory(path)

    outfile = open(path + filename + ".txt", 'w')
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue
        outfile.write("===" + ffind.find_directory_with_filename(filename_list[i]) + "===" + '\n')
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


#   Не знаю как назвать, выводится тип файлов и только один раз, только для ОТСОРТИРОВАННЫХ
def write_data_only_one_writted_type_sorted(data_list, filename_list_sorted, filename, *, prefix=""):
    path = os.path.curdir + directory + prefix + '/'
    create_directory(path)

    outfile = open(path + filename + ".txt", 'w')

    global_ftype = ''
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue

        ftype = ffind.find_filetype(filename_list_sorted[i])
        if ftype != global_ftype:
            global_ftype = ftype
            outfile.write("===" + global_ftype + "===" + '\n')
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


def write_data_to_many_file_witch_sorting_ordering(data_list, filename_list_sorted, filename, *, prefix=""):
    path = os.path.curdir + directory + prefix + '/'
    create_directory(path)

    # outfile = open(path + filename + ".txt", 'w')

    global_ftype = ''
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue

        ftype = ffind.find_filetype(filename_list_sorted[i])
        if ftype != global_ftype:
            global_ftype = ftype
            outfile = open(path + filename + "_" + global_ftype + ".txt", 'w')
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


def write_list(data, filename, *, prefix="", postfix=""):
    path = os.path.curdir + directory + prefix + '/' + postfix + '/'
    create_directory(path)

    outfile = open(path + filename + ".txt", 'w')
    for line in data:
        outfile.write(line + '\n')
    outfile.close()


def create_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

