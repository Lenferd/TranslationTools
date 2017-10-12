#!/usr/bin/python3

# -*- coding: utf-8 -*-

#   Программа:  Json unpack
#   Назначение: Разбирает json файл
#   Версия:     1.1
#   Дата:       15.04.17
#   Модифиц:    22.04.17
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

dit_json = r"input_json" + splitter
dir_result_events = r"result_json" + splitter
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


def get_deep_data(data_dict, flags_l, ignore_l, lvl):
    result_key = []
    result_value = []
    result_lvl = []

    if type(data_dict) is not dict:
        print(data_dict)
        return result_key, result_value, result_lvl

    for key, value in data_dict.items():
        # print(lvl, "   ", value, type(value))
        if type(value) is list:
            for i in range(len(value)):
                temp_key, temp_val, temp_lvl = get_deep_data(value[i], flags_l, ignore_l, lvl + 1)
                result_key.extend(temp_key)
                result_value.extend(temp_val)
                result_lvl.extend(temp_lvl)

        elif type(value) is dict:
            temp_key, temp_val, temp_lvl = get_deep_data(value, flags_l, ignore_l, lvl + 1)
            result_key.extend(temp_key)
            result_value.extend(temp_val)
            result_lvl.extend(temp_lvl)
        else:
            # print(value)
            if key is None or value is None or type(key) is None:
                continue
            elif key in flags_l and value != "" and value not in ignore_l:
                result_key.append(key)
                result_value.append(value.replace('\r', '\\r').replace('\n', "\\n"))
                result_lvl.append(">" * lvl)
    return result_key, result_value, result_lvl


def unpack_file(dir_with_data, name):

    key_list_file = dir_with_data + dir_flags + "flags.txt"
    ignore_name_file = dir_with_data + dir_flags + "ignore.txt"
    filename = dir_with_data + dit_json + name
    out_path = dir_with_data + dir_result_events

    flags = read_flags(key_list_file)
    ignore = read_flags(ignore_name_file)

    flags = flags.get(filename.split(splitter)[-1])
    ignore = ignore.get(filename.split(splitter)[-1])
    if flags is None:
        print("Don't have flags for this file")
        exit(-1)
    if ignore is not None:
        print("Ignoring string: ", ignore)
    else:
        print("No ignored str")
        ignore = []

    print("Flags for this file: ", flags)

    # read file
    with open(filename, "r", encoding="UTF8") as f:
        names_list = ''.join([line.strip() for line in f if line.strip()])

    # read as json
    j_obj = json.loads(names_list)

    json_list = [["Key"], ["Value"], ["lvl"]]
    # print(json_list[1][0])

    for i in range(len(j_obj)):
        g_temp_key, g_temp_val, g_temp_lvl = get_deep_data(j_obj[i], flags, ignore, 1)
        json_list[0] += g_temp_key
        json_list[1] += g_temp_val
        json_list[2] += g_temp_lvl


    # print(json_list[0])
    # for k, v in zip(json_list[0], json_list[1]):
    #     for i in range(len(k)):
        # print(k, "\t", v)

    outfile = open(out_path + filename.split(splitter)[-1].split(".")[0] + ".txt", 'w', encoding="UTF8")
    for k, v, l in zip(json_list[0], json_list[1], json_list[2]):
        outfile.write(l + "\t" + k + "\t" + v + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        dir_with_data = def_data_fold
    else:
        dir_with_data = sys.argv[1]
        name = sys.argv[2]

    unpack_file(dir_with_data, name)
