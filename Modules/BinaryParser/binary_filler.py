#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  binary filler
#   Назначение: Заполнение бинарного файла
#   Версия:     1.0
#   Дата:       10.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

MIN_STR = 2
MAX_STR = 1024000
DEBUG = False

from Modules.BinaryParser import binary_checker as bcheck
from Modules.BinaryParser import binary_parser
from Modules.FilesOperation import create_directory
from Modules.FilesOperation import find
from Modules.FilesOperation import read_binary_file


def parse_and_fill_binary_list(binary_list, orig_binary_data, trans_binary_data, binary_file_list, outpath):

    binary_file_counter = 0
    for binary_file in binary_list:
        print(binary_file)
        binary = read_binary_file(binary_file)
        i = 0
        binary_size = len(binary)

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
            size = binary_parser.parse_size_bloc(byte_size)

            #   check our limits
            if not bcheck.is_size_in_the_boundaries(size, min_lenght=MIN_STR, max_lenght=MAX_STR):
                i += 4
                continue

            # check out of boundarie
            if not bcheck.is_out_of_boundaries(i, size, binary_size):
                i += 4
                continue

            # after string (if its not divided by 4) we should find zero cell. Example: sd00
            end_block = i + 4 + size - 1

            # check fake symbol in string
            byte_str = binary[i + 4:end_block + 1]

            # check 00 in str
            if not bcheck.is_not_have_system_in_str(byte_str):
                i += 4
                continue

            #############
            #   have:
            #   i - pointer str start
            #   end_block - pointer to last cell
            #
            #   try to find equal str in our binary_data

            diff = 0
            selected_line = 0
            while selected_line < len(orig_binary_data):
                if len(orig_binary_data[selected_line]) == size:
                    if orig_binary_data[selected_line] == byte_str:
                        diff = replace_binary_str(i, i+4, end_block, orig_binary_data.pop(selected_line),
                                                  trans_binary_data.pop(selected_line), size, binary, debug=byte_str)
                    else:
                        selected_line += 1
                        continue
                # elif len(orig_binary_data[selected_line]) - size < 4:
                #     if check_str_without_end_spaces(orig_binary_data[selected_line], byte_str) is not None:
                #         diff = replace_binary_str(i, i+4, end_block, orig_binary_data.pop(selected_line),
                #                                   trans_binary_data.pop(selected_line), size, binary,debug=byte_str)
                else:
                    selected_line += 1
                    continue

            if diff == 0:
                i += 4
            else:
                i += diff + 4
            while i % 4 != 0:
                i += 1

        #   outfile name

        create_directory(outpath)
        outfile_name = find.find_filename(binary_file_list[binary_file_counter])
        outfile = open(outpath + '/' + outfile_name, 'wb')
        outfile.write(binary)
        binary_file_counter += 1


def convert_text_to_binary(text_data):
    result_bin_list = []
    for text in text_data:
        temp = text.replace('\\r', '\r').replace('\\n', "\n")
        result_bin_list.append(bytearray(temp, encoding="UTF8"))
    return result_bin_list


def replace_binary_str(position_start, position_text, position_end, orig_data, transl_data, orig_size, data, *, debug):
    # Сколько добавляем пробелов из-за добавления ру строки (4-x блочность)
    plust_empty_space = b' ' * calculate_space_size(orig_data, transl_data)
    # К нашей результирующей строке перевода добавляем пробелы
    transl_data += plust_empty_space
    # Высчитываем разницу в символов (для изменения размера строки)(пробелы в конце иногда удаляются)
    diff = len(orig_data) - orig_size
    # Заменяем строчку
    data = data[0:position_text] + orig_data + data[position_end + 1:]

    # Меняем размер
    new_size = len(transl_data) + diff
    try :
        if new_size >= 256:
            size2 = new_size // 256
            temp_new_size = new_size - 256 * size2
            data[position_start] = temp_new_size
            data[position_start + 1] = size2
        else:
            data[position_start] = new_size
    except ValueError:
        print('****')
        print(len(orig_data))
        print(debug)
        print('====')
        print(orig_data)
        print(orig_size)
        print(transl_data)
        print(len(transl_data))
        print(new_size)
        print(diff)

    return new_size


def calculate_space_size(original_data, transl_data):
    size = (len(original_data) % 4) - (len(transl_data) % 4)
    if size < 0:
        size+=4
    return size


def check_str_without_end_spaces(binary_line, byte_str):
    temp_binary = byte_str.rstrip()
    if temp_binary == binary_line:
        return True
    else:
        return False
