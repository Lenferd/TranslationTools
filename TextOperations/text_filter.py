#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  text filter
#   Назначение: Фильтрация текста, удаление лишних строк (системных)
#   Версия:     1.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)
import copy
import re
from FilesOperation import find as ffind


def ordering_by_filetype(text_data, files_name):
    local_text_data = copy.deepcopy(text_data)
    local_file_name = copy.deepcopy(files_name)

    ordered_data = []
    ordered_filelist = []
    type_list = ffind.find_all_type(local_file_name)

    for ftype in type_list:
        j = 0
        while j < len(local_text_data):
            filetype = ffind.find_filetype(local_file_name[j])
            if filetype == ftype:
                ordered_data.append(local_text_data.pop(j))
                ordered_filelist.append(local_file_name.pop(j))
            else:
                j += 1

    return ordered_data, ordered_filelist


def filter_text(text_data, *,
                h_symbols=True,
                n_system_str=True, n_merged_reg=True, n_more_three_upcase=True, n_underscore=True):
    removed_lines = []
    result_lines = []

    for text in text_data:
        local_lines = []
        local_removed_lines = []

        for line in text:
            if h_symbols:
                if is_have_only_numbers_or_symbols(line):
                    local_removed_lines.append("OnS:\t" + line)  # don't have letter
                    continue
            if n_system_str:
                if is_have_unity_system_string(line):
                    local_removed_lines.append("USy:\t" + line)  # Unity system
                    continue
            if n_merged_reg:
                if is_have_different_registry_merged_words(line):
                    local_removed_lines.append("MeW:\t" + line)  # Merged words
                    continue
            if n_more_three_upcase:
                if is_have_three_upcase(line):
                    local_removed_lines.append("UpC:\t" + line)  # Upcase str
                    continue
            if n_underscore:
                if is_have_underscore(line):
                    local_removed_lines.append("UnS:\t" + line)  # have underscore
                    continue

            local_lines.append(line)

        result_lines.append(local_lines)
        removed_lines.append(local_removed_lines)

    return result_lines, removed_lines


#   {"id"
def get_quotes_blocks_with_text(text_data, *, start_pattern=r""):
    removed_lines = []
    result_lines = []

    for text in text_data:
        local_lines = []
        local_removed_lines = []

        for line in text:
            if not is_start_equal_pattern(line, start_pattern):
                local_removed_lines.append(line)  # Not equal start NEQ
                continue
            if not is_have_close_quotes_at_edge(line):
                local_removed_lines.append(line)  # Not closed quotes NCQ
                continue

            local_lines.append(line)

        removed_lines.append(local_removed_lines)
        result_lines.append(local_lines)
    return result_lines, removed_lines


def oxenfree_filter_resources(text_data):  # text_data is list of lists
    return filter_text(text_data,
                       h_symbols=True,
                       n_system_str=True, n_merged_reg=True, n_more_three_upcase=True, n_underscore=True)


def oxenfree_filter_lvl(text_data, *, start_str=r""):
    quotes_str, quotes_removed = get_quotes_blocks_with_text(text_data, start_pattern=start_str)

    result_lines, removed_lines = filter_text(quotes_removed,
                                              h_symbols=True,
                                              n_system_str=True, n_merged_reg=True, n_more_three_upcase=True,
                                              n_underscore=True)
    return quotes_str, result_lines, removed_lines


# filter abcCde   (merged low and big case)
def is_have_different_registry_merged_words(line):
    # except for \n
    if re.search(r".*\\n.*", line) is not None:
        return False

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


def is_start_equal_pattern(line, pattern):
    if re.search(pattern, line) is not None:
        return True
    else:
        return False


# {}
def is_have_close_quotes_at_edge(line):
    if re.search(r"\{.*\}", line) is not None:
        return True
    else:
        return False
