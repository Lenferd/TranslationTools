#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  il unpacker
#   Назначение: запаковка il файлов
#   Автор:      Lenferd (DeysonSH@gmail.com)

import os
import sys
import unittest

sys.path.insert(0, os.path.join("..", ".."))
from Modules.FilesOperation import readFile
from Modules.FilesOperation import find
from Modules.FilesOperation import writeFile
from il_unpacker import replacePlus

directory = "input_il"

def replace_translation(data, data_orig, data_transl):
    assert(len(data) != 0)
    assert(len(data_orig) == 3)
    assert(len(data_orig) == len(data_transl))
    assert(len(data_orig[2]) == len(data_transl[2]))

    for i in range(len(data_orig[0])):
        assert(data_orig[0][i] == data_transl[0][i])
        assert(data_orig[1][i] == data_transl[1][i])

    for i_d in range(len(data)):
        if (data[i_d].find("ldstr") != -1):
            for j_t in range(len(data_orig[0])):
                if (data[i_d].find(data_orig[1][j_t]) != -1 and data[i_d].find(data_orig[2][j_t]) != -1):
                    data[i_d] = data[i_d].replace(data_orig[2][j_t], data_transl[2][j_t])
    return data

def main():
    file_il = find.get_file_from_directory(directory)
    file_orig = find.get_file_from_directory("input_origin_il")
    file_transl = find.get_file_from_directory("input_translated_il")

    with open(file_il, 'r', encoding="CP1251") as file:
        data = file.read()
    assert(len(data) != 0)
    data = replacePlus(data)
    data = data.split('\n')
    assert(len(data) != 0)

    data_orig = [[],[],[]]
    data_transl = [[],[],[]]

    with open(file_orig, 'r', encoding="UTF8") as infile:
        for line in infile:
            data_orig[0].append(line.strip().split('\t')[0])
            data_orig[1].append(line.strip().split('\t')[1])
            data_orig[2].append(line.strip().split('\t')[2])

    with open(file_transl, 'r', encoding="UTF8") as infile:
        for line in infile:
            data_transl[0].append(line.strip().split('\t')[0])
            data_transl[1].append(line.strip().split('\t')[1])
            data_transl[2].append(line.strip().split('\t')[2])

    data = replace_translation(data, data_orig, data_transl)

    outfile = open(os.path.join("result_il_bin", os.path.basename(file_il)), 'w', encoding="CP1251")
    for line in data:
        outfile.write(line + '\n')
    outfile.close()

class DLLPackTests(unittest.TestCase):
    def test_replacing(self):
        test_text = '''    IL_000d:  stloc.1
            IL_000e:  ldloc.1
            IL_000f:  brfalse.s  IL_001c

            IL_0011:  ldstr      "Target is null"
            IL_0016:  newobj     instance void [mscorlib]System.InvalidOperationException::.ctor(string)
            IL_001b:  throw
        '''
        expected_text = '''    IL_000d:  stloc.1
            IL_000e:  ldloc.1
            IL_000f:  brfalse.s  IL_001c

            IL_0011:  ldstr      "Тархет из нулл"
            IL_0016:  newobj     instance void [mscorlib]System.InvalidOperationException::.ctor(string)
            IL_001b:  throw
        '''
        original = [["IL_0011:"], ["ldstr"], ["Target is null"]]
        translation = [["IL_0011:"], ["ldstr"], ["Тархет из нулл"]]
        self.assertEqual(replace_translation(test_text.split('\n'), original, translation), expected_text.split('\n'))


if __name__ == '__main__':
    main()
    # unittest.main()
