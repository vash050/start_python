import math


# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_pow(x, y):
    """ функция возводит в отрицательную степень y"""

    result = 1
    while 0 > y:
        result *= x
        y += 1
    return 1 / result


print(my_pow(10, -5))
print(pow(10, -5))  # проверка