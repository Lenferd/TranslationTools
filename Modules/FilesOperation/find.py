#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  find
#   Назначение: Модуль для поиска файлов и организации названий файлов
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import re
import os


def find_filename(long_path):
    return long_path[long_path.rfind("/") + 1:]


#   TODO не уверен, что он работает
def find_directory_name(long_path):
    buf = long_path[:long_path.rfind("/")]
    buf = buf[buf.rfind("/") + 1:]
    return buf


def find_directory_with_filename(long_path):
    return find_directory_name(long_path) + "/" + find_filename(long_path)


def find_empty_files(data_list, filename_list):
    empty_files = []
    for i in range(len(data_list)):
        if len(data_list[i]) == 0:
            empty_files.append(filename_list[i])
    return empty_files


def find_filetype(long_path):
    return long_path[long_path.rfind(".")+1:]


def find_all_type(filename_list):
    datatype_list = []
    for file in filename_list:
        datatype_list.append(file[file.rfind(".")+1:])
    datatype_list = list(set(datatype_list))
    datatype_list.sort(key=natural_keys)
    return datatype_list


def construct_file_three(path, *, ignoring_directories=[]):
    files_list = []
    # first - find files in root dir

    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files_list.append(os.path.join(path, item))

    dirs_list = os.listdir(path=path)
    for directory in dirs_list:
        if directory in ignoring_directories:
            continue
        for root, dirs, files in os.walk(path + '/' + directory):
            for name in files:
                files_list.append(os.path.join(root, name))
    return files_list


def get_file_from_directory(fullpath):
    if len(os.listdir(fullpath)) > 1:
        print("There are many files, not one!")
        exit(-1)
    elif len(os.listdir(fullpath)) < 1:
        print("No one files :(")
        exit(-1)
    else:
        return os.path.join(fullpath, os.listdir(fullpath)[0])


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split('(\d+)', text)]

