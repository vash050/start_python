# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

my_dist = {}
with open('z_3.txt', 'r', encoding='utf-8') as f_obj:
    while True:
        content = f_obj.readline().split()
        if content:
            my_dist[content[0]] = content[1]
        else:
            break
print(my_dist)
sum_salary = 0
count = 0
for key, value in my_dist.items():
    if int(value) < 20000:
        print(key)
    sum_salary += int(value)
    count += 1
print(sum_salary/count)
