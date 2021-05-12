# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, data_in):
        self.data_in = data_in

    def __str__(self):
        return f'{self.data_in}'

    @classmethod
    def transformations_str_to_int(cls, data_in):
        to_int = list(map(int, data_in.split('-')))
        return to_int

    @staticmethod
    def check_validity_date(data_int):
        my_list_data_num = Data.transformations_str_to_int(data_int)
        if 1900 < my_list_data_num[2] < 2100:
            if 0 < my_list_data_num[1] < 13:
                if 0 < my_list_data_num[0] < 32:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


class MyData(Data):
    pass


person_1 = MyData('22-12-1952')
print(person_1)
print(type(person_1))
print(person_1.transformations_str_to_int('22-12-1952'))
print(Data.check_validity_date('10-25-1952'))

