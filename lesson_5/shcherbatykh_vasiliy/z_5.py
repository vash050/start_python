import random
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers = ' '.join(list(map(str, [random.randint(0, 100) for num in range(150)])))

with open('z_5.txt', 'x') as f_obj:  # создаем файл и запиываем в него
    f_obj.write(numbers)

with open('z_5.txt', 'r') as f_obj:  # читаем файл и получаем сумму чисел
    content = f_obj.readline().split()
    numbers = sum(map(int, content))
print(numbers)
