#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  delete file
#   Назначение: Удаление файлов
#   Версия:     2.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os


#   @parma del_list contain full path
def del_file_from_list(del_list):
    for file in del_list:
        os.remove(file)
