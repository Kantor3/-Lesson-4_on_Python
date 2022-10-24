"""
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
"""
import my_Lib as my
import random
from functools import reduce

'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''
print('Формируем список уникальных элементов последовательности чисел')

while True:
    seq_size = my.get_InputNumber(0, txt='\nВведите размер последовательности', end='-')
    if my.check_exit(seq_size):
        break

    seq_numbs = [random.randint(1, seq_size) for rnd in range(seq_size)]
    print(f'\nЗаданная последовательность чисел -> {seq_numbs}')

    # Способ-1 (использование set)
    print(f'Уникальные элементы заданной последовательности чисел -> {list(set(seq_numbs))} (вариант set)')

    # Способ-2 (использование filter и reduce)
    seq_unq = list(filter(lambda el: not (el is None),
                          reduce(lambda lst, el: lst + [el if not (el in lst) else None], seq_numbs, [])))
    print(f'Уникальные элементы заданной последовательности чисел -> {seq_unq} (вариант. filter + reduce)')
