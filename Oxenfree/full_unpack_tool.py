#!/usr/bin/python3

# -*- coding: utf-8 -*-
#   Программа:  full_unpack_tool
#   Назначение: Производит комплекс операций по извлечению текста из распакованных файлов игры
#   Версия:     1.0
#   Дата:       21.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import sys
sys.path.insert(0, os.path.pardir)

from Modules.FilesOperation.writeFile import create_directory

# print(os.getcwdb())
# print(os.getcwd())
# print(os.getcwdu())
# sys.path.append(os.getcwdu()/)
# print(sys.path)

def_data_fold = r"../Oxenfree_data/"
def_dir = "../Oxenfree_data/test/"

if __name__ == '__main__':

    dir_with_data = ""

    if len(sys.argv) < 2:
        dir_with_data = def_dir
    else:
        dir_with_data = def_data_fold + sys.argv[1] + "/"
        # os.system("bash " + def_data_fold + "init.bat" + " " + sys.argv[1])

    # On the first we should unpack resources files

    os.system("python oxenfree_binary_unpack_resources.py " + dir_with_data);

    # Unpack lvl files

    os.system("python oxenfree_binary_unpack_lvl.py " + dir_with_data);