#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  delete file
#   Назначение: Удаление файлов
#   Версия:     2.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
from FilesOperation import find as ffind


#   @param del_list contain full path
def del_file_from_list(del_list):
    for file in del_list:
        os.remove(file)


#   @param del_list contain type of file
def del_file_from_list_of_types(del_list, directory):
    file_list = ffind.construct_file_three(directory)
    for ftype in del_list:
        for file in file_list:
            if ffind.find_filetype(file) == ftype:
                os.remove(file)
