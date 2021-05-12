# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# str_list = []
# while True:
#     str_from = input("введите строки: ")
#     if str_from:
#         str_list.append(f'{str_from}\n')
#     else:
#         break

str_list = [
    'His fate was destined to a foreign strand,\n',
    'A petty fortress and an "humble" hand;\n',
    'He left the name at which the world grew pale\n',
    'To point a moral, or adorn a TALE.\n'
]

with open("text.txt", "x") as f_obj:
    f_obj.writelines(str_list)
