# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = [1, 2.2, 'str', [1, 'str'], {'key': 'value'}, {"a", "b"}, True, (5, 'el'), 5]

# вариант первый не правельный

# my_list = []
# i = 0
# while i < 10:
#     element = input('введите 10 значений по очереди:')
#     my_list.append(element)
#     i += 1

# вариант правельный

# my_list = []
# for i in range(1, 10):
#     element = input('введите 10 значений по очереди:')
#     my_list.append(element)

for idx, value in enumerate(my_list[:]):
    if (idx + 1) % 2 == 0:
        my_list[idx - 1], my_list[idx] = my_list[idx], my_list[idx - 1]
print(my_list)
