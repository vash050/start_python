# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки Pen {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки Pencil {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки Handle {self.title}')


draw_1 = Pen('Red')
draw_1.draw()

draw_2 = Pencil('Yellow')
draw_2.draw()

draw_3 = Handle('Blue')
draw_3.draw()
