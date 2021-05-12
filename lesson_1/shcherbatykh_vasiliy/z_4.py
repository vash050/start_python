# 4) Пользователь вводит целое положительное число.
#    Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.

# num = int(input('введите положительное число: '))
num = int('12459785')
number_big = 0

while num > 0:
    number = num % 10
    if number > number_big:
        number_big = number
    num //= 10

print(f'Самая большая цифра: {number_big}')
