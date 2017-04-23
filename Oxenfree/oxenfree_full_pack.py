#!/usr/bin/python3

# -*- coding: utf-8 -*-
#   Программа:  full_unpack_tool
#   Назначение: Производит комплекс операций по запаковке текста
#   Версия:     1.0
#   Дата:       23.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import sys

sys.path.insert(0, os.path.pardir)

from Modules.FilesOperation.find import get_file_from_directory

def_data_fold = r"../Oxenfree_data/"
def_dir = "../Oxenfree_data/GOG-2.2P/"


if __name__ == '__main__':

    dir_with_data = ""

    if len(sys.argv) < 2:
        dir_with_data = def_dir
    else:
        dir_with_data = os.path.join(def_data_fold, sys.argv[1])

    # File with translation
    file_dialog_text = get_file_from_directory(os.path.join(dir_with_data, "input_dialogs"))
    file_lvl_text = get_file_from_directory(os.path.join(dir_with_data, "input_lvl"))
    file_resources_text = get_file_from_directory(os.path.join(dir_with_data, "input_resources"))

    # File with origin data
    origin_file_dialog_text = get_file_from_directory(os.path.join(dir_with_data, "orig_dialogs"))
    origin_file_lvl_text = get_file_from_directory(os.path.join(dir_with_data, "orig_lvl"))
    origin_file_resources_text = get_file_from_directory(os.path.join(dir_with_data, "orig_resources"))
    origin_dialog_to_transl = get_file_from_directory(os.path.join(dir_with_data, "origin_dialog_to_transl"))

    input_dialog_repacked = os.path.join(dir_with_data, "input_dialog_repacked", "input_dialog_repacked.txt")

    print("Start dialog retranslate")
    os.system("python ../Tools/Block_handler/pack_block.py "
              + origin_dialog_to_transl + " "
              + origin_file_dialog_text + " "
              + file_dialog_text + " "
              + input_dialog_repacked)
    print("Dialog retranslate done")
    print("")

    print("Retranslate lvl using dialogs")
    os.system("python oxenfree_packer.py "
              + os.path.join(dir_with_data, "input_lvl_binaries") + " "
              + origin_dialog_to_transl + " "
              + input_dialog_repacked + " "
              + os.path.join(dir_with_data, "input_lvl_binaries2"))
    print("Pack dialogs to lvl done")
    print("")

    print("Retranslate lvl using text")
    os.system("python oxenfree_packer.py "
              + os.path.join(dir_with_data, "input_lvl_binaries2") + " "
              + origin_file_lvl_text + " "
              + file_lvl_text + " "
              + os.path.join(dir_with_data, "result_lvl"))
    print("Packs lvl_text to lvl done")
    print("")

    print("Retranslate resources")
    os.system("python oxenfree_packer.py "
              + os.path.join(dir_with_data, "input_resources_binaries") + " "
              + origin_file_resources_text + " "
              + file_resources_text + " "
              + os.path.join(dir_with_data, "result_resources"))
    print("Packs resources to resources done")
    print("")

