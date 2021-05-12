# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# для наглядности сделал первые два параметра обязательными


def print_date_person(name, surname, **kwargs):
    """Выводит данные пользователя"""
    print(f"'name': '{name}', 'surname': '{surname}', {str(kwargs)[1:-2]}'")  # пропадает последняя ковычка '


date_person = {
    'surname': 'Smit',
    'birthdate': '12.06.1998',
    'email': 'MaxSmit@mail.com',
    'phone': '+4552522555',
    'name': 'Max'
}
print_date_person(**date_person)