#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Чиним возможные проблемы с кодировками
#   Версия:     1.0
#   Дата:       11.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


def fix_coding_line(line):
    result_line = line.replace(r"\u201c", r"“").replace(r"\u201d", r"”")
    result_line = result_line.replace(r"\u2019", r"’").replace(r"\u2026", r"…")
    return result_line


def fix_codign_list(str_list):
    data_out = []
    for line in str_list:
        data_out.append(fix_coding_line(line))
    return data_out


def revert_line_coding_fix(line):
    resullt_line = line.replace(r"“", r"\u201c").replace(r"”", r"\u201d")
    resullt_line = resullt_line.replace(r"’", r"\u2019").replace(r"…", r"\u2026")
    return resullt_line


def revert_fix_coding(str_list):
    data_out = []
    for line in str_list:
        data_out.append(revert_line_coding_fix(line))
    return data_out
