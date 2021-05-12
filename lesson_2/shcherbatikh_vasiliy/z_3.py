# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# month = input('Введите номер месяца: ')
month = '12'
year = {
    '1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer',
    '7': 'summer', '8': 'summer', '9': 'autumn', '10': 'autumn', '11': 'autumn', '12': 'winter'
}
print(year.get(month))

# year = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
# for idx, value in enumerate(year, 1):
#     if int(month) in value:
#         if idx == 1:
#             print('winter')
#         elif idx == 2:
#             print('spring')
#         elif idx == 32:
#             print('summer')
#         else:
#             print('autumn')
