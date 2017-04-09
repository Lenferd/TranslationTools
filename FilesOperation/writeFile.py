#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  write file
#   Назначение: Запись данных в файлы
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os


def write_data(data_list, filename):
    outfile = open(os.path.curdir + "/result/" + filename + ".txt", 'w')
    for data in data_list:
        for line in data:
            outfile.write(line + '\n')
    outfile.close()


def write_data_with_filename(data_list, filename_list, filename):
    outfile = open(os.path.curdir + "/result/" + filename + ".txt", 'w')
    for i in range(len(data_list)):
        outfile.write("===" + find_directory_with_filename(filename_list[i]) + "===" + '\n')
        if len(data_list[i]) == 0:
            outfile.write("***EMPTY FILE***\n")
        for line in data_list[i]:
            outfile.write(line + '\n')
    outfile.close()


def find_filename(long_path):
    return long_path[long_path.rfind("/") + 1:]


#   TODO не уверен, что он работает
def find_directory_name(long_path):
    buf = long_path[:long_path.rfind("/")]
    buf = buf[buf.rfind("/") + 1:]
    return buf


def find_directory_with_filename(long_path):
    return find_directory_name(long_path) + find_filename(long_path)


def find_empty_files(data_list, filename_list):
    empty_files = []
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            empty_files.append(filename_list[i])
    return empty_files


def write_list(data, filename):
    outfile = open(os.path.curdir + "/files_info/" + filename + ".txt", 'w')
    for line in data:
        outfile.write(line + '\n')
    outfile.close()
