import functools
import sys

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

my_list = (el for el in range(100, 1001) if el % 2 == 0)


def my_func(num_1, num_2):
    """
    функция принемает 2 числа и возращяет их произведение
    :param num_1: number
    :param num_2: number
    :return: number
    """
    return num_1 * num_2


print(functools.reduce(my_func, my_list))
print(sys.getsizeof(my_list))
