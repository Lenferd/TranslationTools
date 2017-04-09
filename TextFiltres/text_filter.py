#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  text filter
#   Назначение: Фильтрация текста, удаление лишних строк (системных)
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)
import re
from FilesOperation import find as ffind


def ordering_by_filetype(text_data, files_name):
    ordered_data = []
    ordered_filelist = []
    type_list = ffind.find_all_type(files_name)

    i = 0
    while i < len(text_data):
        templ_filetype = ffind.find_filetype(files_name[i])
        ordered_data.append(text_data.pop(i))
        ordered_filelist.append(files_name.pop(i))

        j = 0
        while j < len(text_data):
            filetype = ffind.find_filetype(files_name[j])
            if filetype == templ_filetype:
                ordered_data.append(text_data.pop(j))
                ordered_filelist.append(files_name.pop(j))
            else:
                j += 1

    return ordered_data, ordered_filelist


def oxenfree_filter(text_data):  # text_data is list of lists
    removed_lines = []
    result_lines = []

    for text in text_data:
        local_lines = []
        local_removed_lines = []

        for line in text:
            if is_have_only_numbers_or_symbols(line):
                local_removed_lines.append("OnS: " + line)  # don't have letter
                continue
            if is_have_unity_system_string(line):
                local_removed_lines.append("UnS: " + line)  # Unity system
                continue
            if is_have_different_registry_merged_words(line):
                local_removed_lines.append("MeW: " + line)  # Merged words
                continue
            if is_have_three_upcase(line):
                local_removed_lines.append("UpC: " + line)  # Upcase str
                continue
            if is_have_underscore(line):
                local_removed_lines.append("UnS: " + line)  # have underscore
                continue

            local_lines.append(line)

        result_lines.append(local_lines)
        removed_lines.append(local_removed_lines)

    return result_lines, removed_lines


# filter abcCde   (merged low and big case)
def is_have_different_registry_merged_words(line):
    if re.search(r".*[a-z][A-Z].*", line) is None:
        if re.search(".*[a-z][A-Z][a-z].*", line) is None:
            return False
    return True


# filter 938434 or ././;
def is_have_only_numbers_or_symbols(line):
    if re.search(r".*[a-zA-Z].*", line) is None:
        return True
    else:
        return False


# Unity system    System.out....
def is_have_unity_system_string(line):
    if re.search(r".*\w\.\w.*", line) is not None:
        return True
    else:
        return False


# REN CLARISSSA
def is_have_three_upcase(line):
    if re.search(r".*[A-Z][A-Z][A-Z].*", line) is not None:
        return True
    else:
        return False

# Boat_8PM_Ren
def is_have_underscore(line):
    if re.search(r".*_.*", line) is not None:
        return True
    else:
        return False
