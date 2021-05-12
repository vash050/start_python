# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# реализовал программу в которой ввод прирываеться символом 'n', любой символом не являющимся числом
# вызовет сообщение о не корректном вводе, на написание программы ушло около 2 часов.


def checking_correct_input(list_numbers_from_in_func):
    """
    функция проверяет все ли введенные символы числа
    :param list_numbers_from_in_func: list
    :return: list with bool
    """
    return list(map(lambda el: el.isdigit(), list_numbers_from_in_func))


def sum_numbers(str_numbers_input, all_sum_numbers_in_func):
    """
    функция принемает строку, переводит ее в числа, суммирует, выводит и возвращяет сумму
    :param all_sum_numbers_in_func: int сумма приходит
    :param str_numbers_input: str
    :return: int сумма
    """
    all_sum_numbers_in_func += sum(map(int, str_numbers_input))
    print(all_sum_numbers_in_func)
    return all_sum_numbers_in_func


all_sum_numbers = 0
while True:
    # str_numbers_from = input('введите числа через пробел или n для выхода: ').split()
    str_numbers_from = '123 452 524 123 896 n'.split()

    if str_numbers_from[-1].upper() == 'N':  # проверяем на команду для закрытия программы
        sum_numbers(str_numbers_from[:-1], all_sum_numbers)  # суммируем и закрываем
        break

    list_correct = checking_correct_input(str_numbers_from)  # проверяем коректность ввода

    if all(list_correct):
        all_sum_numbers = sum_numbers(str_numbers_from, all_sum_numbers)  # суммируем и запрашиваем продолжение
    else:
        print('Введите цифры или символ n для закрытия программы: ')
