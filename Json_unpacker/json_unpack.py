#!/usr/bin/python3

# -*- coding: utf-8 -*-

#   Программа:  Json unpack
#   Назначение: Разбирает json файл
#   Версия:     1.0
#   Дата:       15.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

# filename = r"./input/test.json"
filename = r"./input/events.json"
import json
from FilesOperation import readFile

with open(filename, "r", encoding="UTF8") as f:
    names_list = ''.join([line.strip() for line in f if line.strip()])
# infile = open(filename, 'r')
# data = ""
# for line in infile:
#     data += line.strip()

# print(names_list)

# print(data)
# print(names_list)
# outfile = open("kek.txt", 'w')
# outfile.writelines(names_list[0])
j_obj = json.loads(names_list)
# print(j_obj)

# i = 0
for i in range(len(j_obj)):
    if j_obj[i]["Description"] != None and j_obj[i]["Description"] != "":
        j_obj[i]["Description"] = u'L1-' + str(i) + ': ' + j_obj[i]["Description"]

    # for obj in j_obj:
    #     i+=1;
    #     print(obj["Name"])
    #     print(obj["Description"])
    # print(obj.keys())
# print(i)

outfile = open("events.json", 'w', encoding="UTF8")
outfile.write(json.dumps(j_obj, ensure_ascii=False))
#
outfile = open("events_clean.json", 'w', encoding="UTF8")
outfile.write(json.dumps(j_obj, sort_keys=True, indent=4, ensure_ascii=False))
