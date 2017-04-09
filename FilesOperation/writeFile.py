#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  write file
#   Назначение: Запись данных в файлы
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import FilesOperation.find as find


def write_data(data_list, filename):
    outfile = open(os.path.curdir + "/result/" + filename + ".txt", 'w')
    for data in data_list:
        for line in data:
            outfile.write(line + '\n')
    outfile.close()


def write_data_with_filename(data_list, filename_list, filename):
    outfile = open(os.path.curdir + "/result/" + filename + ".txt", 'w')
    for i in range(len(data_list)):
        outfile.write("===" + find.find_directory_with_filename(filename_list[i]) + "===" + '\n')
        if len(data_list[i]) == 0:
            outfile.write("***EMPTY FILE***\n")
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


def write_data_with_filename_wo_empty(data_list, filename_list, filename):
    outfile = open(os.path.curdir + "/result/" + filename + ".txt", 'w')
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            continue
        outfile.write("===" + find.find_directory_with_filename(filename_list[i]) + "===" + '\n')
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


def write_list(data, filename):
    outfile = open(os.path.curdir + "/files_info/" + filename + ".txt", 'w')
    for line in data:
        outfile.write(line + '\n')
    outfile.close()
