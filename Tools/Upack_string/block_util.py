#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Назначение: Функции для работы непосредственно с блоками
#   Версия:     1.0
#   Дата:       10.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)


def oxf_is_same_size(position, orig, string):
    i = position
    size = 0
    try:
        while orig[i] != '\"' or orig[i + 1] != ',':
            size += 1
            i += 1
        i -= 1
        while orig[i] == ' ':
            size -= 1
            i -= 1
        if size == len(string):
            return True
        else:
            return False
    except IndexError:
        print(orig)


def oxf_have_right_prefix(position, data):
    if data[(position - len("\"name\":\"left\",\"value\":\"")):position] == "\"name\":\"left\",\"value\":\"":
        return True
    elif data[(position - len("\"name\":\"right\",\"value\":\"")):position] == "\"name\":\"right\",\"value\":\"":
        return True
    elif data[(position - len("\"name\":\"top\",\"value\":\"")):position] == "\"name\":\"top\",\"value\":\"":
        return True
    return False


def oxf_search_string(string):
    i = 0
    dataresult = []
    while i < len(string):
        teststring = string[i:i + 22]
        if ((teststring.find("\"name\":\"left\",\"value\"") != -1)
                or (teststring.find("\"name\":\"right\",\"value\"") != -1)
                or (teststring.find("\"name\":\"top\",\"value\"") != -1)):
            i += 22
            while string[i] != '\"':
                i += 1
            i += 1
            resultstring = ''
            while (string[i] != '\"') or (string[i + 1] != ','):
                resultstring += string[i]
                i += 1
            dataresult.append(resultstring + '\n')
        i += 1
    return dataresult
