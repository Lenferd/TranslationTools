#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  binary checker
#   Назначение: Проверка бинарных данных
#   Версия:     2.0
#   Дата:       8.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


def is_block_can_be_size(data):
    if data[2] == 0 and data[3] == 0:  # i don't think string may be more then ???
        if (data[0] > 0 and data[1] >= 0) or (data[0] == 0 and data[1] > 0):  # 12 || 10 and 01
            return True
    return False


def is_out_of_boundaries(start_position, size, bytearray_size):
    if start_position + 3 + size < bytearray_size:
        return True
    else:
        return False


def is_start_string_dont_have_system_symbols(data):
    if data[0] > 31 and data[1] > 31:
        return True
    else:
        return False


def is_size_in_the_boundaries(size, *, min_lenght=1, max_lenght):
    if min_lenght <= size <= max_lenght:
        return True
    else:
        return False


def is_not_have_system_in_str(data):
    test = data.find(b'\x00')
    return True if test < 0 else False
