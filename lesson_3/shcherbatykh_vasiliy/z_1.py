# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division_num(num_1, num_2):
    """
    :param num_1: number
    :param num_2: number
    :return: number or warning
    """
    if num_2 == 0:
        print('На ноль делить нельзя!!!')
        return
    return num_1 / num_2


number_1 = 14
number_2 = 7
print(division_num(number_1, number_2))
