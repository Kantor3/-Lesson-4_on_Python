"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import my_Lib as my
import random
from functools import reduce


# Преобразование числа в верхний индекс для отражения в виде степени к-л числа
def get_superscript(numb, rev=None):
    numb_str = str(numb)
    ns = '0123456789'
    ss = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    res = numb_str.maketrans(' '.join(ns), ' '.join(ss)) if rev is None else \
        numb_str.maketrans(' '.join(ss), ' '.join(ns))
    return numb_str.translate(res)


# Формирование элемента многочлена
def form_pln(l_ratios):
    gen_el = lambda i, k: f'{k if k and (k > 1 or not i) else ""}{"x" if i > 0 else ""}' \
                          f'{f"{get_superscript(i)}" if i > 1 else ""}' if k else ''
    el_polynom = (gen_el(i, k) for i, k in enumerate(l_ratios) if k)
    return reduce(lambda pln, el: pln + f' + {el}', el_polynom)


'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''

if __name__ == '__main__':

    name_file = 'file_task4.txt'
    k_from = 0
    k_to = 10

    print('Формируем многочлен степени k с случайно сгенерированными коэффициентами и записываем его в файл')
    while True:
        d_k = my.get_InputNumber(0, txt='\nЗадайте натуральную степень многочлена', end='-')
        if my.check_exit(d_k):
            break

        # Формирование многочлена
        ratios = [random.randint(k_from, k_to) for rnd in range(d_k + 1)]
        polynomial = form_pln(ratios)
        print(f'По заданным коэффициентам {ratios} сформирован многочлен -> {polynomial}')

        # Запись многочлена в файл
        fil = open(name_file, 'w')
        fil.close()
        with open(name_file, 'a', encoding='utf8') as fil:
            fil.writelines(polynomial)
