#!/usr/bin/python3

# -*- coding: utf-8 -*-

#   Программа:  Json pack
#   Назначение: Разбирает json файл
#   Версия:     1.0
#   Дата:       22.04.17
#   Модифиц:
#   Автор:      Lenferd (DeysonSH@gmail.com)

import json
import sys
import os

if os.name == "nt":
    splitter = "\\"
else:
    splitter = "/"

# filename = r"./input/test.json"
# filename = r"./input/events.json"
# filename = r"../../SunlessSea_data/test1/input_json/test.json"
def_data_fold = r"../../SunlessSea_data/version1/"

dir_json = r"input_json" + splitter
dir_json_text = r"input_json_text" + splitter
dir_json_text_orig = r"input_json_text_orig" + splitter
dir_result_json = "result_json_bin"
dir_flags = r"input_flags" + splitter

name = r"events.json"
# filename = r"../../SunlessSea_data/version1/input_json/events-norm.json"

dir_with_data = ""

def read_flags(file):
    result_dict = {}
    infile = open(file, "r", encoding="UTF8")
    name = ""
    data = []
    for line in infile:
        line = line.rstrip()
        # print(line)
        if line.find(".json") != -1:
            name = line
        elif line != "":
            data.append(line)
        else:
            result_dict.update({name : list(data)})
            name = ''
            data.clear()
    if name != '':
        result_dict.update({name: list(data)})

    # for k, v in result_dict.items():
    #     print(k, v)
    return result_dict


def deep_data_translate(data_dict, flags_l, ignore_l, lvl, orig, transl):
    if type(data_dict) is dict:
        for key, value in data_dict.items():
            # print(lvl, "   ", value, type(value))
            if type(value) is list:
                for i in range(len(value)):
                    deep_data_translate(value[i], flags_l, ignore_l, lvl + 1, orig, transl)

            elif type(value) is dict:
                deep_data_translate(value, flags_l, ignore_l, lvl + 1, orig, transl)
            else:
                if key is None or value is None or type(key) is None:
                    continue
                elif key in flags_l and value != "" and value not in ignore_l:
                    # print(value)
                    # print(orig[2])
                    if value.rstrip() in orig[2]:
                        # print("???")
                        # print(value)
                        index = orig[2].index(value.rstrip())
                        if key == transl[1][index] and ">" * lvl == transl[0][index]:
                            # print("yess")
                            data_dict.update({key: transl[2].pop(index)})
                            orig[0].pop(index)
                            orig[1].pop(index)
                            orig[2].pop(index)
                            transl[0].pop(index)
                            transl[1].pop(index)
                            # lvl.pop(index)
    else:
        print(data_dict)


def pack_file(dir_with_data, name):
    key_list_file = dir_with_data + dir_flags + "flags.txt"
    ignore_name_file = dir_with_data + dir_flags + "ignore.txt"

    filename_transl = os.path.join(dir_with_data, dir_json_text, name + '.txt')
    filename_origin = dir_with_data + dir_json_text_orig + name + '.txt'
    filename_json = dir_with_data + dir_json + name + '.json'

    # print(filename_transl)
    out_path = os.path.join(dir_with_data, dir_result_json)
    # out_path = dir_with_data + dir_result_json

    flags = read_flags(key_list_file)
    ignore = read_flags(ignore_name_file)

    # print(flags)
    flags = flags.get(filename_json.split(splitter)[-1])
    ignore = ignore.get(filename_json.split(splitter)[-1])
    if flags is None:
        print("Don't have flags for this file")
        print(key_list_file)
        exit(-1)
    if ignore is not None:
        print("Ignoring string: ", ignore)
    else:
        print("No ignored str")
        ignore = []

    print("Flags for this file: ", flags)

    # Read text transl
    json_text_transl = [["Key"], ["Value"], ["lvl"]]
    infile = open(filename_transl, "r", encoding="UTF8")

    for line in infile:
        json_text_transl[0].append(line.split("\t")[0].rstrip().replace('\\r', '\r').replace('\\n', "\n"))
        json_text_transl[1].append(line.split("\t")[1].rstrip().replace('\\r', '\r').replace('\\n', "\n"))
        json_text_transl[2].append(line.split("\t")[2].rstrip().replace('\\r', '\r').replace('\\n', "\n"))

    # Read orig text

    json_text_orig = [["Key"], ["Value"], ["lvl"]]
    infile = open(filename_origin, "r", encoding="UTF8")

    for line in infile:
        json_text_orig[0].append(line.split("\t")[0].rstrip().replace('\\r', '\r').replace('\\n', "\n"))
        json_text_orig[1].append(line.split("\t")[1].rstrip().replace('\\r', '\r').replace('\\n', "\n"))
        json_text_orig[2].append(line.split("\t")[2].rstrip().replace('\\r', '\r').replace('\\n', "\n"))

    # Check
    if len(json_text_transl[0]) != len(json_text_orig[0]):
        print("Size of files not equal!")
        print("Origing size: ", len(json_text_orig[0]), "\tTranslated file: ", len(json_text_transl[0]))
        exit(-1)

    # Read json
    with open(filename_json, "r", encoding="UTF8") as f:
        names_list = ''.join([line.strip() for line in f if line.strip()])

    # read as json
    j_obj = json.loads(names_list)

    # print(j_obj)
    for i in range(len(j_obj)):
        deep_data_translate(j_obj[i], flags, ignore, 1, json_text_orig, json_text_transl)

    outfile = open(os.path.join(out_path, "events.json"), 'w', encoding="UTF8")
    outfile.write(json.dumps(j_obj, ensure_ascii=False))

    outfile = open(os.path.join(out_path, "events_clean.json"), 'w', encoding="UTF8")
    outfile.write(json.dumps(j_obj, sort_keys=True, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        dir_with_data = def_data_fold
    else:
        dir_with_data = sys.argv[1]
        name = sys.argv[2]

    pack_file(dir_with_data, name)
