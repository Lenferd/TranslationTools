#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  il unpacker
#   Назначение: Распаковка il файлов
#   Версия:     1.0
#   Дата:       23.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


import sys
import os
import re
import unittest

sys.path.insert(0, os.path.join("..", ".."))
from Modules.FilesOperation import readFile
from Modules.FilesOperation import find

directory = "input_il"

def replacePlus(text):
    return re.sub(
        r'"\s*\n\s*\+\s*"',
        '',
        text
    )

def unpackText(text):
    text = replacePlus(text)
    pattern = re.compile(r'(IL.+?:)'
                        + r'\s*?'
                        + r'(ldstr)'
                        + r'\s*?'
                        + r'(".*?")'
                        # + r'\s*\n*\s*'
                        # + r'\+*' + r'\s*?'
                        # + r'(".*")*' + r'\s*'
                        )
    return pattern.findall(text)

def main():
    filename = find.get_file_from_directory(directory)

    with open(filename, 'r', encoding="CP1251") as file:
        data = file.read()

    result_data = unpackText(data)

    # print(result_data)
    outfile = open(os.path.join(".", "result_il", os.path.basename(filename) + ".txt"), 'w', encoding="UTF8")
    #
    for i in range(len(result_data)):
        outfile.write(str(result_data[i][0]) + "\t" + str(result_data[i][1]) + "\t" + str(result_data[i][2]) + '\n')
    # writeFile.write_list(result_data, os.path.basename(file), path=os.path.join('.', "result_il"))


if __name__ == '__main__':
    main()
    # unittest.main()
