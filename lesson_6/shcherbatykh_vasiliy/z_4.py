# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Car {self.color} {self.name} has speed {self.speed} km')

    def go(self):
        print(f'car {self.color} {self.name} go')

    def stop(self):
        print(f'car {self.color} {self.name} stop')

    def turn(self, direction):
        print(f'car {self.color} {self.name} turn {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Attention, you exceed the speed limit of 60 km/h')
        print(f'Car {self.color} {self.name} has speed {self.speed} km')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Attention, you exceed the speed limit of 40 km/h')
        print(f'Car {self.color} {self.name} has speed {self.speed} km')


class PoliceCar(Car):
    pass


car_1 = TownCar(65, 'red', 'mazda', False)
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.stop()

car_2 = SportCar(200, 'yellow', 'BMW', False)
car_2.go()
car_2.show_speed()
car_2.turn('left')
car_2.stop()

car_3 = WorkCar(45, 'blue', 'Ford', False)
car_3.go()
car_3.show_speed()
car_3.turn('right')
car_3.stop()

car_4 = PoliceCar(45, 'White', 'Hammer', True)
car_4.go()
car_4.show_speed()
car_4.turn('right')
car_4.stop()
