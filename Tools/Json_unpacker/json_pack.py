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

# name = r"events.json"
# filename = r"../../SunlessSea_data/version1/input_json/events-norm.json"

dir_with_data = ""


class JsonPack:
    # Files in
    key_list_file = ""
    ignore_name_file = ""
    filename_transl = ""
    filename_origin = ""
    filename_json = ""

    # json file name
    name = ""

    # Path out
    out_path = ""

    # Flags
    flags = 0
    ignore = 0

    # json
    j_obj = 0

    # texts
    json_text_orig = 0
    json_text_transl = 0

    def init_data(self, json_obj, flags, ignore, text_orig, text_transl):
        self.j_obj = json_obj
        self.flags = flags
        self.ignore = ignore
        self.json_text_orig = text_orig
        self.json_text_transl = text_transl

    def init(self, _dir_with_data, _name):
        print(_dir_with_data)
        print(_name)
        self.name = _name
        self.key_list_file = _dir_with_data + dir_flags + "flags.txt"
        self.ignore_name_file = _dir_with_data + dir_flags + "ignore.txt"
        self.filename_transl = os.path.join(_dir_with_data, dir_json_text, _name + '.txt')
        self.filename_origin = _dir_with_data + dir_json_text_orig + _name + '.txt'
        self.filename_json = _dir_with_data + dir_json + _name + '.json'
        self.out_path = os.path.join(_dir_with_data, dir_result_json)

        self.flags = self.read_flags(self.key_list_file)
        self.ignore = self.read_flags(self.ignore_name_file)

        self.flags = self.flags.get(self.filename_json.split(splitter)[-1])
        self.ignore = self.ignore.get(self.filename_json.split(splitter)[-1])

        if self.flags is None:
            print("Don't have flags for this file")
            print(self.key_list_file)
            exit(-1)
        if self.ignore is not None:
            print("Ignoring string: ", self.ignore)
        else:
            print("No ignored str")

        print("Flags for this file: ", self.flags)

    @staticmethod
    def replace_on_dict(line, dic):
        for i, j in dic.items():
            line = line.replace(i, j)
        return line

    # because we can have some \r\n at the end, is removed in compare orig vs origin, but
    # for translated text we don't have to do this
    @staticmethod
    def read_file_full_strip(filename):
        text = [[], [], []]
        infile = open(filename, "r", encoding="UTF8")

        replace_dict = {"\\r": "\r", "\\n": "\n", "\\t": "\t",  "\\\"": "\""}
        for line in infile:
            text[0].append(
                JsonPack.replace_on_dict(line.split("\t")[0], replace_dict).rstrip()
            )
            text[1].append(
                JsonPack.replace_on_dict(line.split("\t")[1], replace_dict).rstrip()
            )
            text[2].append(
                JsonPack.replace_on_dict(line.split("\t")[2], replace_dict).rstrip()
            )

        infile.close()
        return text

    @staticmethod
    def read_file(filename):
        text = [[], [], []]
        infile = open(filename, "r", encoding="UTF8")

        replace_dict = {"\\r": "\r", "\\n": "\n", "\\t": "\t",  "\\\"": "\""}
        for line in infile:
            text[0].append(
                JsonPack.replace_on_dict(line.split("\t")[0].rstrip(), replace_dict)
            )
            text[1].append(
                JsonPack.replace_on_dict(line.split("\t")[1].rstrip(), replace_dict)
            )
            text[2].append(
                JsonPack.replace_on_dict(line.split("\t")[2].rstrip(), replace_dict)
            )

        infile.close()
        return text

    def read_files_to_pack(self):
        # read
        self.json_text_transl = self.read_file(self.filename_transl)
        self.json_text_orig = self.read_file_full_strip(self.filename_origin)

        # Check
        if len(self.json_text_transl[0]) != len(self.json_text_orig[0]):
            print("Size of files not equal!")
            print("Origing size: ", len(self.json_text_orig[0]), "\tTranslated file: ", len(self.json_text_transl[0]))
            exit(-1)

    def read_json(self):
        # Read json
        with open(self.filename_json, "r", encoding="UTF8") as f:
            names_list = ''.join([line.strip() for line in f if line.strip()])

        # read as json
        self.j_obj = json.loads(names_list)

    def read_flags(self, file):
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
                result_dict.update({name: list(data)})
                name = ''
                data.clear()
        if name != '':
            result_dict.update({name: list(data)})

        infile.close()
        # for k, v in result_dict.items():
        #     print(k, v)
        return result_dict

    def deep_data_translate(self, data_dict, flags_l, ignore_l, lvl, _orig,  _trans):
        if type(data_dict) is dict:
            for key, value in data_dict.items():
                # print(lvl, "   ", value, type(value))
                if type(value) is list:
                    for i in range(len(value)):
                        self.deep_data_translate(value[i], flags_l, ignore_l, lvl + 1, _orig,  _trans)

                elif type(value) is dict:
                    self.deep_data_translate(value, flags_l, ignore_l, lvl + 1, _orig,  _trans)
                else:
                    if key is None or value is None or type(key) is None:
                        continue
                    # find correct value to translate
                    elif key in flags_l and value != "" and value not in ignore_l:
                        # find all index in original list
                        padding = 0
                        while True:
                            try:
                                index = _orig[2].index(value.rstrip(), padding)
                                padding = index + 1
                                # print("padding {}".format(padding))
                                # print("index {}".format(index))
                            except ValueError:
                                break
                            if key == _trans[1][index] and ">" * lvl == _trans[0][index]:
                                # print("yess")
                                # print(transl[2][index])
                                data_dict.update({key:  _trans[2].pop(index)})
                                _orig[0].pop(index)
                                _orig[1].pop(index)
                                _orig[2].pop(index)
                                _trans[0].pop(index)
                                _trans[1].pop(index)
                                break
        else:
            print(data_dict)

    def translate(self):
        for i in range(len(self.j_obj)):
            self.deep_data_translate(self.j_obj[i], self.flags, self.ignore, 1,
                                     self.json_text_orig, self.json_text_transl)

    def write_out(self):
        outfile = open(os.path.join(self.out_path, self.name + ".json"), 'w', encoding="UTF8")
        outfile.write(json.dumps(self.j_obj, ensure_ascii=False))
        outfile.close()

        outfile = open(os.path.join(self.out_path, self.name + "_clean.json"), 'w', encoding="UTF8")
        outfile.write(json.dumps(self.j_obj, sort_keys=True, indent=4, ensure_ascii=False))
        outfile.close()

    def write_out_not_translated(self):
        outfile = open(os.path.join(self.out_path, self.name + "_not_translated" + ".txt"), 'w', encoding="UTF8")

        transl = self.json_text_transl
        orig = self.json_text_orig

        outfile.writelines(["lvl: {}\nKey: {}\nValue: {}\nOrig: {}\n\n".format(
            transl[0][i], transl[1][i], transl[2][i], orig[2][i]) for i in range(len(transl[0]))])
        outfile.close()



def pack_file(_dir_with_data, _name):
    json_pack = JsonPack()
    # print(_dir_with_data)
    # print(_name)
    json_pack.init(_dir_with_data=_dir_with_data, _name=_name)
    json_pack.read_files_to_pack()
    json_pack.read_json()
    json_pack.translate()
    json_pack.write_out()
    json_pack.write_out_not_translated()

if __name__ == '__main__':
    name = ""
    if len(sys.argv) < 3:
        dir_with_data = def_data_fold
    else:
        dir_with_data = sys.argv[1]
        name = sys.argv[2]

    # json_pack = JsonPack
    # json_pack.init(_dir_with_data = dir_with_data, _name=name)
    # json_pack.read_files()
    # json_pack.read_json()
    # json_pack.translate()
    # json_pack.write_out()
    # json_pack.pack_file(dir_with_data, name)
