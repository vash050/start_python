# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    arg_default = [200, 10, 1]
    if len(argv) == 4:
        arg_default = argv[1:4]
    elif len(argv) == 2:
        arg_default[0] = argv[1]
    elif len(argv) == 3:
        arg_default[0], arg_default[1] = argv[1], argv[2]
    print(int(arg_default[0]) * int(arg_default[1]) + int(arg_default[2]))
except ValueError:
    print('введите цифрами отработанные часы, ставку, премию')
