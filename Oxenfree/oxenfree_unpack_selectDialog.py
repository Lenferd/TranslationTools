#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Программа:  unpack select dialog
#   Назначение: Вытаскиваем текст из строк с кавычками и прочей дрянью
#   Версия:     2.0
#   Дата:       9.04.17
#   Автор:      Lenferd (DeysonSH@gmail.com)

from Modules.FilesOperation import find

path = "./result/lvl_to_transl/quotes/separated"

if __name__ == '__main__':
    list_of_files = find.construct_file_three(path)


