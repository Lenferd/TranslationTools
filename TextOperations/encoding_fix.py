#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Чиним возможные проблемы с кодировками
#   Версия:     1.0
#   Дата:       11.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


def fix_coding_line(line):
    result_line = fix_quotes(line)
    result_line = fix_symbols(result_line)
    return result_line


def fix_codign_list(str_list):
    data_out = []
    for line in str_list:
        data_out.append(fix_coding_line(line))
    return data_out


def fix_quotes(line):
    return line.replace(r"\u201c", r"“").replace(r"\u201d", r"”")


def fix_symbols(line):
    return line.replace(r"\u2019", r"’")