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
    echo "folder name = " ${folder_name}
fi

mkdir ${folder_name}
cd ${folder_name}

# Folders

# In
mkdir input_json
mkdir input_flags
mkdir input_json_text
mkdir input_json_text_orig

# Out
mkdir result_json
mkdir result_json_bin

echo "Press Enter to exit"
read A