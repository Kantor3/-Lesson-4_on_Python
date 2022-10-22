"""
Вычислить число (π) c заданной точностью d
Пример:
- при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}
"""
import my_Lib as my
import random


# Самый быстрый из известных методов - Алгоритм Чудновского
# основанный на π-формулах Рамануджана
def pi_thudnov(max_iter=100):
    C = 426880 * 10005 ** 0.5
    d_Lq = 545140134
    d_L0 = 13591409
    d_Xq = -262537412640768000
    sum_series, Lq, Xq, Mq = 0, d_L0, 1, 1
    for q in range(max_iter):
        sum_series += Mq * Lq / Xq
        Lq += d_Lq
        Xq *= d_Xq
        Mq *= (6 * q + 1) * (6 * q + 3) * (6 * q + 5) * (2 / (q + 1)) ** 3
        res = C / sum_series
        yield res, q + 1


# Модифицированная формула Лейбница - Метод основан на π = 6 * arctan((1/3)^0,5} -
def gen_Leibniz(max_iter):
    C = 12 ** 0.5
    d_numer = -1/3
    sum_series, numer, res = 0, 1, C
    for q in range(max_iter):
        sum_series += numer / (1 + 2 * q)
        numer *= d_numer
        res = C * sum_series
        yield res, q + 1


# Использование метода Монте-Карло
def gen_MonteCarlo(max_iter=1000000):
    cnt = 0
    for q in range(1, max_iter):
        x = random.random()
        y = random.random()
        cnt += 1 if x ** 2 + y ** 2 < 1 else 0
        res = 4 * (cnt / q)
        yield res, q


def pi(precision, method=1, max_iteration=50):
    divider = 10 ** (-precision)
    pi_spec_acc = 3.141592653589793238462643383279 // divider

    if method == 1:                             # Модифицированная формула Лейбница
        gen_pi = gen_Leibniz(max_iteration)
    elif method == 2:                           # Метод Монте-Карло
        gen_pi = gen_MonteCarlo(max_iteration)
    elif method == 7:                           # Алгоритм Чудновского
        gen_pi = pi_thudnov(max_iteration)
    else:
        return method, None

    for pi_refund in gen_pi:
        if pi_refund[0] // divider == pi_spec_acc:
            #
            # print(f'pi_refund[0] // divider = {pi_refund[0] // divider}, pi_spec_acc = {pi_spec_acc}')
            #
            return pi_refund
    else:
        return method, False


'''
=====================================================================================
Расчет числа Пи без использования специальной функции возвращающей собственно число π
Используем модифицированнцю формулу Лейбница, которая дает результат с точность до 10 
знаков после запятой за 20 итераций. 
Первые 10 знаков числа π: 3.1415926535    
Первые 156 знаков числа π: 
3.14159265358979
3.14159265358980
32384626433832795028841971693993751058209749445923078164062862
089986280348253421170679821480865132823066470938446095505822317253594081284811
# ====================================================================================
'''
print('Вычисляем число π c заданной точностью [10^{-1} ≤ d ≤10^{-14}]')

while True:
    params = my.get_InputTuple('\nУкажите требуюмую точность вычисления числа π (число знаков после запятой)',
                               'Выберите метод расчета числа π: '
                               '(1 - модиф. формула Лейбница; 2 - Монте-Карло; 7 - Алгоритм Чудновского)',
                               'Укажите максимальное количество итераций', end='-')
    if my.check_exit(params):
        break

    accuracy, method, iterations = params
    number_pi, count_iter = pi(accuracy, method=method, max_iteration=iterations)
    if count_iter is None:
        print(f'Указанный для расчета Метод = №{number_pi} не найден')
    elif type(count_iter) is bool:
        print(f'Число π c точностью {1 / 10 ** accuracy} '
              f'за разумное число итераций вычислить c использованием метода {number_pi} НЕ удалось!')
    else:
        print(f'Число π (c точностью {1 / 10 ** accuracy}, '
              f'расчитанное за {count_iter} итераций) = '
              f'{str(number_pi)[:accuracy+2]}')


"""
Доугие методы расчета числа π, в т.ч. с самым быстрым приближением
"""
# Использование метода Монте-Карло через лямбда-функцию
# pi_calc = lambda N: 4 * reduce(lambda cnt, _:
#                                cnt + (1 if random.random() ** 2 + random.random() ** 2 < 1 else 0), range(N)) / N
