# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('z_4_source.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()

numbers = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
new_list = []
for idx, value in enumerate(content[:]):
    my_str = value.split()
    my_str[0] = numbers[idx]
    new_list.append(' '.join(my_str))
    new_list.append('\n')
print(new_list)
with open('z_4_finish.txt', 'x', encoding='utf-8') as f_obj_1:
    f_obj_1.writelines(new_list)
