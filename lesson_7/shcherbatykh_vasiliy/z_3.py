# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (
# __mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно. Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение. Умножение. Создается общая клетка из двух. Число ячеек общей
# клетки определяется как произведение количества ячеек этих двух клеток. Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток. В классе
# необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
# позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество
# ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд
# записываются все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда
# метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в
# ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, cells_cell):
        self.cells_cell = cells_cell

    def check(self, other):
        return type(self) == Cell and type(other) == Cell

    def __add__(self, other):
        if self.check(other):
            return self.cells_cell + other.cells_cell

    def __sub__(self, other):
        if self.check(other) and self.cells_cell >= other.cells_cell:
            return self.cells_cell - other.cells_cell
        else:
            return f'разность меньше или равна 0'

    def __mul__(self, other):
        if self.check(other):
            return self.cells_cell * other.cells_cell

    def __truediv__(self, other):
        if self.check(other):
            return self.cells_cell // other.cells_cell

    def str_stars(self, count_stars):
        str_cell = '*' * count_stars
        return str_cell

    def make_order(self, count_cell_row):
        rest_str = self.cells_cell % count_cell_row
        full_str = self.cells_cell // count_cell_row
        counter = 0
        str_full_result = ''
        while counter < full_str:
            str_full_result += f'{self.str_stars(count_cell_row)}\n'
            counter += 1
        str_full_result += f'{self.str_stars(rest_str)}'
        return str_full_result


cell_first = Cell(12)
cell_second = Cell(5)
print(cell_first + cell_second)
print(cell_first - cell_second)
print(cell_first * cell_second)
print(cell_first / cell_second)
print(cell_first.make_order(5))

