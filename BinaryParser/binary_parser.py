#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  binary parser
#   Назначение: Обработка бинарных данных
#   Версия:     2.0
#   Дата:       8.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

from BinaryParser import binary_checker as bcheck

MIN_STR = 2
MAX_STR = 1024000
DEBUG = False

def parse_size_bloc(data):
    return data[0] + 256 * data[1]


def parse_binary_list(binary_list):
    datas_list = []

    for binary in binary_list:

        i = 0
        binary_size = len(binary)
        local_data_list = []

        while i < binary_size - 4:  # last block cannot be the size cell
            #   fist check can it be string size
            #   all time i % 4 == 0
            if i % 4 != 0:
                print("ERROR! Wrong start pointer")

            byte_size = binary[i:i + 4]
            #   check can be our size
            if not bcheck.is_block_can_be_size(byte_size):
                i += 4
                continue

            # getSize
            size = parse_size_bloc(byte_size)

            #   check our limits
            if not bcheck.is_size_in_the_boundaries(size, min_lenght=MIN_STR, max_lenght=MAX_STR):
                i += 4
                continue

            #   check out of boundarie
            if not bcheck.is_out_of_boundaries(i, size, binary_size):
                i += 4
                continue

            # after string (if its not divided by 4) we should find zero cell. Example: sd00
            end_block = i + 4 + size - 1

            # TODO ЭТО НЕ БУДЕТ РАБОТАТЬ С МОИМ КОСТЫЛЁМ НА РАЗМЕР!
            # if end_block % 4 != 0:
            #     if not binary[end_block + 1] == 0:
            #         print("WARNING! MAY BE WRONG. SEE THE DEBUG")
            #         i += 4
            #         continue

            # check fake symbol in string
            byte_str = binary[i + 4:end_block+1]

            if DEBUG:
                print("===")
                print("binary:")
                print(binary)
                print("byte_str:")
                print(byte_str)
                print("size:")
                print(size)
            # checked only fist two symbol
            if not bcheck.is_start_string_dont_have_system_symbols(byte_str[0:2]):
                i += 4
                continue

            #
            #   Now we are read str
            #

            try:
                string = byte_str.decode("UTF-8")
            except UnicodeDecodeError:
                print("error decode")
                print(byte_str)
                i += 4
                continue

            # after all
            i += 4
            local_data_list.append(string)

        datas_list.append(local_data_list)
    return datas_list