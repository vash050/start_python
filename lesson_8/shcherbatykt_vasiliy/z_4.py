# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


class Repository:
    def __init__(self, *args, **kwargs):
        self.product = None
        self.quantity = None
        self.date_in = None
        self.date_out = None

    def append_to_repository(self):
        pass

    def transmit_to_out(self):
        pass


class OfficeEquipment:
    def __init__(self, *args, **kwargs):
        self.equipment_class = args[0]
        self.type = args[1]
        self.brand = args[2]
        self.model = args[3]
        self.id = args[4]

    def __str__(self):
        return f'{self.equipment_class} {self.type} {self.brand} {self.model} {self.id}'


class Scanner(OfficeEquipment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dpi = args[5]

    def __str__(self):
        return f'{self.equipment_class} {self.type} {self.brand} {self.model} {self.id} {self.dpi}'


class Copier(OfficeEquipment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.copying_speed = args[5]

    def __str__(self):
        return f'{self.equipment_class} {self.type} {self.brand} {self.model} {self.id} {self.copying_speed}'


class Printer(OfficeEquipment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = args[5]

    def __str__(self):
        return f'{self.equipment_class} {self.type} {self.brand} {self.model} {self.id} {self.color}'


product_1 = Printer('printer', 'laser', 'Canon', 'i-SENSYS LBP6030B', '252245', 'bw')
print(product_1)
print(type(product_1))
