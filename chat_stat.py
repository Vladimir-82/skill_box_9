# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# from zipfile import ZipFile
# from StringIO import StringIO
#
#
# unzip_file = StringIO(ZipFile('python_snippets/vovoyna-i-mir.txt.zip').extractall())
# with open(unzip_file, mode=r, encoding='cp1251') as file:
#     chars = {}
#     for char in file:
#         if char.isdigit():
#             if chars[char]:
#                 chars[char] += 1
#             else:
#                 chars[char] = 1
# print(chars)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

import os
LETTERS = 'а б в г д е ж з и к л м н о п р с т у ф к ц ч ш щ ъ ь э ю я'.split()
file = 'kr'
file = open(file, 'r', encoding='utf8')
file_content = file.read()
for letter in LETTERS:
    if letter in file_content:
        print(f'{letter:*^3}, {file_content.count(letter):*^10}')
# if 'Юранд' in file_content:
#     print(file_content.count('Юранд'))