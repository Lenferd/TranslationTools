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
