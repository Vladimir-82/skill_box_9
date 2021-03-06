# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
file_name = 'log_file.txt'
file_exit='file_exit.txt'
file = open(file_name, mode='r', encoding='utf8')
file_exit = open(file_exit, mode='w', encoding='utf8')

content_list = []

for line in file.readlines():
    if 'NOK' in line:
        content = line[0:17:] + ']'
        content_list.append(content)


for content in sorted(set(content_list)):
    file_exit.write((content) + ' ' + str(content_list.count(content)))
    file_exit.write('\n')
file.close()
file_exit.close()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828