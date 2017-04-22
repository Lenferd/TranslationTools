#!/bin/bash
folder_name=$1

#   Программа:     directory creator
#   Назначение:    Создает структуру для использования инструментов (иерархию папок)
#   Использование: Для использования необходимо переместить в папку *_data и в mkdir указать создаваемые папки
#   Версия:        1.0
#   Дата:          22.04.17
#   Автор:         Lenferd (DeysonSH@gmail.com)


if [${folder_name} == ""]
    then echo "Directory name not set"
    exit
else
    echo folder name = %folder_name%
fi

mkdir ${folder_name}
cd ${folder_name}

# There we can "mkdir" a new directories
# mkdir list


read A