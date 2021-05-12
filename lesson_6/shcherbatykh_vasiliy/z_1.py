import time

# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    def __init__(self, green_time=2):
        self.__color = {'red': 7, 'yellow': 2, 'green': green_time}
        self._flag_while = True
        self.standard_colors = ('red', 'yellow', 'green')

    def running(self):

        while self.check():
            for idx, value in self.__color.items():
                print(f'{idx}')
                time.sleep(value)

    def check(self):
        test_color = []
        for el in self.__color:
            test_color.append(el)
        if tuple(test_color) == self.standard_colors:
            return True
        else:
            print(f'не правельный режим работы')
            return False

# вариант который был первым
# class TrafficLight:
#     def __init__(self, green_time=2):
#         self.__color = ['red', 'yellow', 'green']
#         self._t = [7, 2, green_time]
#         self._flag_while = True
#
#     def check(self, count):
#         standard_colors = ('red', 'yellow', 'green')
#         return self.__color[count] == standard_colors[count] and len(self.__color) == 3
#
#     def switches(self, count):
#         if self.check(count):
#             print(self.__color[count])
#             time.sleep(self._t[count])
#         else:
#             print(f'не правельный режим работы, цвета не соответствуют стандарту или их число не равно 3')
#             self._flag_while = False
#
#     def __str__(self):
#         return f'color: {self.__color}, time: {self._t}'
#
#     def running(self):
#         count = 0
#         while self._flag_while:
#             if count < 3:
#                 self.switches(count)
#                 count += 1
#             else:
#                 count = 0


unit_1 = TrafficLight(5)
unit_1.running()
