#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  Binary sieve
#   Назначение: Удаление файлов по списку
#   Версия:     2.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

from FilesOperation import readFile as fread
from FilesOperation import deleteFile as delfile

path = "./Info/remover.txt"

if __name__ == '__main__':
    #   del from list
    del_list = fread.read_file_rstrip(path)
    delfile.del_file_from_list(del_list)

    # del from format
    # del_format = fread.read_file_rstrip(path)
    # delfile.del_file_from_list_of_types(del_format, "D:\TT\TT_OF4\LVL_COPIED")