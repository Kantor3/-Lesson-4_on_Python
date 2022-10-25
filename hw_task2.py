"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""
import my_Lib as my
import numpy as np


# Вариант-1 - расчет определение делителей числа - в одну строку
#     Вход:   Целое число, опция printed = True -  если надо вывести список делителей
#     Выход:  2-а значения: 1-е - Список делителей, 2-е - Признак True/False, True, если 'Простое число"
def det_divisors(number, printed=False):
    divisors = list(filter(lambda i: (i if number % i == 0 else 0) != 0, (i + 1 for i in range(number))))
    if printed:
        print(f'Список делителей числа {number}:\n{divisors}')
    return divisors, not len(divisors) > 2


# Вариант-2. Специальный алгоритм, позволяющий на порядок ускорить расчеты
# Определяем все делители полученного числа
# Используется алгоритм:
# Поиск первичных делителей + Генерация остальных делителей перемножением первичных во всех возможных комбинациях
def my_divisors(number, printed=False, progres=0):
    # Формирование списка первичных делителей
    def primediv(number):
        div = number
        n, prime_lst = 1, []
        while div > n:
            n += 1
            if div % n == 0:
                div //= n
                prime_lst += [n]
                n -= 1
        return prime_lst

    # Основное тело функции:
    # 1) получение первичных делителей
    prime_div = primediv(number)
    prime_unq = list(set(prime_div))
    prime_unq.sort()
    if printed: print(f'Простые множители (первичные делители): {prime_unq}')

    # 2) инициализация начальных значений для реализации перемножения первичных делителей во всех возможных комбинациях
    len_prime = len(prime_div)
    divisors = [1]
    media_div = np.array([[1, 0]])

    # 3) собственно реализация перемножения первичных делителей во всех возможных комбинациях
    while media_div.shape[0] > 0:
        lst_key, lst_div = [], []
        for div, pos in media_div:
            for i in range(pos, len_prime):
                new_div = div * prime_div[i]
                divisors += [new_div]
                if i < len_prime:
                    lst_key += [i + 1]
                    lst_div += [new_div]
        media_div = np.column_stack((lst_div, lst_key))

    #  4) финальная обработка списка полученных делителей:
    #     - устраняем повторы (возможны при числе подряд идущих одинаковых первичных делителей > 2)
    #     - сортируем полученные делители по возрастанию, для удобного их чтения и анализа
    divisors_unq = list(set(divisors))
    divisors_unq.sort()

    if printed:
        print(f'Все:       {divisors_unq}\nЧисло делителей = {len(divisors_unq)}')

    return divisors_unq


'''
=====================================================================================
Основное тело программы:
# ====================================================================================
'''
print('Определяем простые множители (первичные делители) заданного числа N')

while True:
    number = my.get_InputNumber(0, txt='\nВведите любое целое число больше нуля', end='-')
    if my.check_exit(number):
        break

    # Вариант-1 простой в реализации, но длительный для больших чисел
    if not my.check_exit(my.get_InputNumber(txt='\nДля расчета по варианту-1 введите 0', end='-')):
        print('\nРасчет по варианту-1 ...')
        div_1 = det_divisors(number, printed=True)

    # Вариант-2 - быстрый, для больших чисел
    print('\nРасчет по варианту-2 ...')
    title = 'Все делители числа'
    print(f'{title} {number}:')
    print('-'*(len(title) + len(str(number)) + 2))
    divisors = my_divisors(number, printed=True, progres=1)
    print(f'Сумма всех делителей числа {number}: {sum(divisors[:-1])}')
