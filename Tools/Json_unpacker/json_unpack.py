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
# import os

# filename = r"./input/test.json"
# filename = r"./input/events.json"
# filename = r"../../SunlessSea_data/test1/input_json/test.json"
# filename = r"../../SunlessSea_data/version1/input_json/events.json"
filename = r"../../SunlessSea_data/version1/input_json/events-norm.json"

out_path = r"../../SunlessSea_data/test1/result_json/"
key_list_file = r"../../SunlessSea_data/test1/input_flags/flags.txt"


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


def get_deep_data(data_dict, flags_l, lvl):
    result_key = []
    result_value = []
    for key, value in data_dict.items():
        # print(lvl, "   ", value, type(value))
        if type(value) is list:
            for i in range(len(value)):
                temp_key, temp_val = get_deep_data(value[i], flags_l, lvl + 1)
                result_key.extend(temp_key)
                result_value.extend(temp_val)
        if type(value) is dict:
            temp_key, temp_val = get_deep_data(value, flags_l, lvl+1)
            result_key.extend(temp_key)
            result_value.extend(temp_val)
        else:
            # print(value)
            if key is None or value is None or type(key) is None:
                continue
            elif key in flags_l and value != "":
                result_key.append(key)
                result_value.append(value)
    return result_key, result_value


if __name__ == '__main__':

    if len(sys.argv) < 2:
        pass
    else:
        filename = sys.argv[1]

    flags = read_flags(key_list_file)
    flags = flags.get(filename.split("/")[-1])
    if flags is None:
        print("Don't have flags for this file")
        exit(-1)
    print("Flags for this file: ", flags)

    # read file
    with open(filename, "r", encoding="UTF8") as f:
        names_list = ''.join([line.strip() for line in f if line.strip()])

    # read as json
    j_obj = json.loads(names_list)

    json_list = [["Key"], ["Value"]]
    # print(json_list[1][0])

    for i in range(len(j_obj)):
        temp_key, temp_val = get_deep_data(j_obj[i], flags, 0)
        json_list[0] += temp_key
        json_list[1] += temp_val


    # print(json_list[0])
    # for k, v in zip(json_list[0], json_list[1]):
    #     for i in range(len(k)):
        # print(k, "\t", v)

    outfile = open(out_path + "result.txt", 'w', encoding="UTF8")
    for k, v in zip(json_list[0], json_list[1]):
        outfile.write(k + "\t" + v + '\n')
