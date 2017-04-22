#!/usr/bin/python3

# -*- coding: utf-8 -*-
#   Программа:  full_unpack_tool
#   Назначение: Производит комплекс операций по запаковке текста в json файлы
#   Версия:     1.0
#   Дата:       22.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import sys
sys.path.insert(0, os.path.pardir)

if os.name == "nt":
    splitter = "\\"
else:
    splitter = "/"

from Modules.FilesOperation.find import construct_file_three
from Tools.Json_unpacker import json_pack

def_data_fold = r"../SunlessSea_data/"
def_dir = "../SunlessSea_data/version04_2017/"

if __name__ == '__main__':

    dir_with_data = ""

    if len(sys.argv) < 2:
        dir_with_data = def_dir
    else:
        dir_with_data = def_data_fold + sys.argv[1] + "/"
        # os.system("bash " + def_data_fold + "init.bat" + " " + sys.argv[1])

    list_of_json_files = construct_file_three(dir_with_data + "/input_json_text")

    for file in list_of_json_files:
        print("Pack " + file.split(splitter)[-1])
        json_pack.pack_file(dir_with_data, file.split(splitter)[-1].split(".")[0])
        print("Packing done")
        print("==============")


    # os.system("python ")

    # On the first we should unpack resources files

    # print("Start resources unpack process")
    # os.system("python oxenfree_binary_unpack_resources.py " + dir_with_data)
    # print("Finish resources unpack")
    # Unpack lvl files
    #
    # print("Start lvl unpack process")
    # os.system("python oxenfree_binary_unpack_lvl.py " + dir_with_data)
    # print("Finish lvl unpack")
