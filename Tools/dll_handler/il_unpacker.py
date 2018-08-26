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

class DLLUnpackTests(unittest.TestCase):
    def test_got_right_data_from_unpack(self):
        test_text = '''IL_009c:  ldstr      "Packsize Failure"
        IL_00a1:  call       void [UnityEngine]UnityEngine.Debug::Log(object)
        IL_00a6:  nop
        IL_00a7:  ldstr      "[Steamworks.NET] Packsize Test returned false, the"
        + " wrong version of Steamworks.NET is being run in this platform."'''

        self.assertEqual(len(unpackText(test_text)), 2)
        self.assertEqual(unpackText(test_text)[0][2], '"Packsize Failure"')
        self.assertEqual(unpackText(test_text)[1][2], '"[Steamworks.NET] Packsize Test returned false, the wrong version of Steamworks.NET is being run in this platform."')

    def test_plus_replace(self):
        test_text = '''IL_00a7:  ldstr      "[Steamworks.NET] Packsize Test returned false, the"
        + " wrong version of Steamworks.NET is being run in this platform."'''
        expected_result= '''IL_00a7:  ldstr      "[Steamworks.NET] Packsize Test returned false, the wrong version of Steamworks.NET is being run in this platform."'''
        self.assertEqual(replacePlus(test_text), expected_result)

    def test_replace_multiple_time(self):
        test_text = ''' "some text"
        + " some add text"
        "some another text"
        "some new text"
           + " another text"'''
        expected_result =  ''' "some text some add text"
        "some another text"
        "some new text another text"'''
        self.assertEqual(replacePlus(test_text), expected_result)


if __name__ == '__main__':
    main()
    # unittest.main()
