# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

# num = input('введите число: ')
num = '3'
sum_numbers = int(num) + int(num * 2) + int(num * 3)
print(sum_numbers)

# через математику это так? этот вариант не работает при вводе двухзначных чисел
num_1 = int('3')
sum_1 = num_1 + (num_1 * 10 + num_1) + (num_1 * 100 + num_1 * 10 + num_1)
print(sum_1)
