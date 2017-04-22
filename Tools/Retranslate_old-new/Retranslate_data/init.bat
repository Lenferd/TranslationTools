@echo off
::   Программа:     directory creator
::   Назначение:    Создает структуру для использования инструментов (иерархию папок)
::   Использование: Для использования необходимо переместить в папку *_data и в mkdir указать создаваемые папки
::   Версия:        1.0
::   Дата:          21.04.17
::   Автор:         Lenferd (DeysonSH@gmail.com)


set folder_name=%1

if "%folder_name%" == "" (
    echo FAIL: "Directory name not set"
    exit /b 1
) else (
    echo folder name = %folder_name%
)
mkdir %folder_name%
cd %folder_name%

:: There we can "mkdir" a new directories
:: mkdir list

mkdir input_original_text
mkdir input_translated_text
mkdir input_file_to_translate

mkdir result_translated

pause
exit /B