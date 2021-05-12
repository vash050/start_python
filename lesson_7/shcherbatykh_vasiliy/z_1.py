# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

# Проверка учитывает не все варианты. Пытался сделать проверку через len(), не хватило времени разобраться

first_matrix = [
    [5, 2, 12],
    [12, 6, 1],
    [13, 9, 0]
]

second_matrix = [
    [2, 6, 20],
    [1, 9, 0],
    [8, 0, 2]
]

third_matrix = [
    [0, 6, 11],
    [61, 6, 0],
    [8, 0, 9]
]


class Matrix:
    def __init__(self, one_matrix):
        self.any_matrix = one_matrix

    def __str__(self):
        str_matrix = ''
        for element in self.any_matrix:
            str_matrix += f'{element}\n'
        return str_matrix

    def __add__(self, other):

        # if self.check(other):
        try:
            sum_matrix = []
            sum_str = []
            counter_str = 0
            for el in self.any_matrix:
                counter_value = 0
                for value in el:
                    sum_str.append(value + other.any_matrix[counter_str][counter_value])
                    counter_value += 1
                sum_matrix.append(sum_str.copy())
                sum_str.clear()
                counter_str += 1
            return Matrix(sum_matrix)
        except Exception as e:
            print('Матрицы имеют разное количество строк или столбцов')

    # def check(self, other):
    #     try:
    #         check_list = []
    #         # if len(self.any_matrix) == len(other):
    #         count_for_check = 0
    #         for el in self.any_matrix:
    #             if len(el) == len(other[count_for_check]):
    #                 check_list.append(True)
    #                 count_for_check += 1
    #             else:
    #                 check_list.append(False)
    #                 count_for_check += 1
    #         if not all(check_list):
    #             raise
    #     except RuntimeError as e:
    #         print('Матрицы имеют разное количество строк или столбцов')
    #     else:
    #         return True


init_1 = Matrix(first_matrix)
init_2 = Matrix(second_matrix)
init_3 = Matrix(third_matrix)
sun_first_second = init_1 + init_2 + init_3
print(sun_first_second)
