# 5) Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким  финансовым результатом работает фирма
# (прибыль ​ — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# revenue = int(input('Введите доход фирмы:'))
# cost = int(input('Введите издержки фирмы:'))
revenue = int('15000')
cost = int('10000')

if revenue > cost:
    print('Фирма работает с прибылью!')

    profit = revenue - cost
    profitability = profit / revenue * 100
    print(f'рентабельность фирмы: {profitability:.2f} %')

    # number_employees = int(input('Введите число сотрудников: '))
    number_employees = int('5')
    profit_one_employee = profit / number_employees
    print(f'Прибыль на одного сотрудника составила: {profit_one_employee:.2f}')
elif revenue == cost:
    print('фирма работает без убытков и без прибыли')
else:
    print('Фирма работает с убытком')
