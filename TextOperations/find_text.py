#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  text filter
#   Назначение: Поиск фрагментов в тексте
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

import re

# def get_text_from_bloc(data, *, b_prefix = r"", b_start = r"", b_end = r"" ):
#     result_text = []
#     for line in data:
#         text =



# def get_text_from_the_pattern(line, b_prefix = r"", b_start = r"", b_end = r""):
#     pattern = r"" +
#     re.fullmatch()

def test_regexp(line, pattern):
    if re.search(pattern, line) is not None:
        return True
    else:
        return False


def is_have_russian_symbols(line):
    if re.search(r".*[А-я].*", line) is not None:
        return True
    else:
        return False
