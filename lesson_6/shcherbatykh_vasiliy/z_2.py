# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._depth = 0.05

    def counter_weight(self):
        weight_asphalt = self._length * self._width * 0.025 * self._depth
        print(f'{weight_asphalt} t')


counter_first = Road(5000, 20)
counter_first.counter_weight()
