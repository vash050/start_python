# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class My_Error_zero(Exception):
    pass


class My_Error_input(Exception):
    pass


def get_two_numbers():
    try:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
        return num_1, num_2
    except Exception as e:
        raise My_Error_input


def division_two_num(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError as e:
        raise My_Error_zero


def division_num():
    while True:
        try:
            num_1, num_2 = get_two_numbers()
            print(division_two_num(num_1, num_2))
        except My_Error_zero as e:
            print('на ноль делить нельзя')
        except My_Error_input as e_input:
            print('введите число')
        else:
            break


division_num()
