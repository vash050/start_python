# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

salary_engineer = {"wage": 25000, "bonus": 5000}
salary_worker = {"wage": 15000, "bonus": 1000}


class Worker:
    def __init__(self, name, surname, position,  bonus, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position('Ivan', 'Ivanov', 'engineer', wage=salary_engineer['wage'], bonus=salary_engineer['bonus'])
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('Max', 'Mixer', 'worker', wage=salary_worker['wage'], bonus=salary_worker['bonus'])
worker_2.get_full_name()
worker_2.get_total_income()
