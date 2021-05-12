# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#  и возвращает сумму наибольших двух аргументов.


def sum_nums(num_1, num_2, num_3):
    if num_1 > num_2 or num_1 > num_3:
        if num_2 > num_3:
            return num_1 + num_2
        else:
            return num_1 + num_3
    else:
        return num_2 + num_3


print(sum_nums(1, 3, 2))
