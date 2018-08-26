[![Build Status](https://travis-ci.org/Lenferd/TranslationTools.svg?branch=master)](https://travis-ci.org/Lenferd/TranslationTools)

Translation Tools for Sunless Sea and Oxenfree. If you are interested in this tool, feel free to ask me (DeysonSH@gmail.com)

### Комплекс инструментов для перевода

В данный момент присутствует:
1. Распаковка и запаковка бинарных архивов `unity` (целевая игра - Oxenfree)  
    Подробная инструкция в папке Oxenfree
2. Распаковка и запаковка `json` файлов (целевая игра - Sunless Sea)  
    Подробная инструкция в папке Sunless Sea
3. Инструмент для переноса перевода со старого текста на новый  
    Подробная инструкция в папке Tools/Retranslate_old-new
    
#### TO-DO
Общее   
[ ] Загрузка информации для запаковки из csv файла (позволит напрямую использовать данные с google docs используя в кач-ве промежуточной стадии загрузку файла (urllib? Так же вопрос с доступом, использовать request + что-то?)   
[ ] Бинарный распаковщик написан под структуру Oxenfree и использует отдельный поиск специфичной структуры (blocks with dialog text). Написать отдельный инструмент для распаковки,благо функции для этого уже есть. 

Json   
[ ] Фрагменты текста могуть храниться не только ключ:значение но и ключ:[массив значений]. Обработать этот случай.

by Lenferd
