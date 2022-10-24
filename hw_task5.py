"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""
import hw_task4 as get_ss
from functools import reduce


# Считываем данные из файла
def get_data_file(name_file):
    with open(name_file, 'r', encoding='utf8') as f:
        # list_str = list([el for el in f])
        str_read = f.read()
    return str_read


# Проверка является ли строка числом
def is_numeric(s_number):
    try:
        _ = float(s_number)
        return True
    except ValueError:
        return False


# Выравнивание размеров списков с достройкой заданным символом
def alignment_size(lst_1, lst_2, compl_symb=None):
    max_len = max(len(lst_1), len(lst_2))
    lst_1 += [compl_symb] * (max_len - len(lst_1))
    lst_2 += [compl_symb] * (max_len - len(lst_2))
    return lst_1, lst_2


if __name__ == '__main__':

    # Лямбда - элементы реализации суммирования многочленов.
    symb_term = 'x'
    get_lst = lambda polynom: [(f'0{el}'.replace(symb_term, ' ').replace('0-', '-').split()[0], el[-1])
                               for el in polynom.split(' + ')]

    get_degree = lambda el: 0 if is_numeric(el[-1]) else \
                            1 if el[-1] == symb_term else \
                            int(get_ss.get_superscript(el[1], rev=True))

    get_els = lambda cfp, el: [0] * (get_degree(el) - len(cfp)) + [int(el[0]) if int(el[0]) else 1]
    get_cfp = lambda polynom: reduce(lambda cfp, el: cfp + get_els(cfp, el), get_lst(polynom), [])

    '''
    =====================================================================================
    Основное тело программы:
    # ====================================================================================
    '''
    name_file1 = 'file_task4.txt'
    name_file2 = 'file_task5.txt'
    name_file3 = 'file_task4_5.txt'

    print('Формируем результирующий многочлен как сумму многочленов, содержащихся в 2-х файлах')

    # Загрузка данных из файлов
    polynom_1 = get_data_file(name_file1)
    polynom_2 = get_data_file(name_file2)

    print(f'многочлен-1 -> {polynom_1}')
    print(f'многочлен-2-> {polynom_2}')

    # Формирование итогового многочлена как сумма загруженных многочленов
    cfp_1 = get_cfp(polynom_1)
    cfp_2 = get_cfp(polynom_2)

    cfp_1, cfp_2 = alignment_size(cfp_1, cfp_2, compl_symb=0)
    cfp_3 = list(map(lambda c1: c1[0] + c1[1], zip(cfp_1, cfp_2)))
    polynom_3 = get_ss.form_pln(cfp_3)

    print(f'Итоговый   -> {polynom_3}')

    # Запись многочлена в файл
    fil = open(name_file3, 'w')
    fil.close()
    with open(name_file3, 'a', encoding='utf8') as fil:
        fil.writelines(polynom_3)
