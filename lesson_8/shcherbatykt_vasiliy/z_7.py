# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров.
# Проверьте корректность полученного результата.

#  числа вида a+bi, где a,b — вещественные числа, i — мнимая единица[2],
#  то есть число, для которого выполняется равенство: i^{2}=-1


class ComplexNumber:
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __str__(self):
        return f'{str(self.complex_number)}'

    @staticmethod
    def get_complex_num(complex_number):
        return map(int, str(complex_number)[1:-2].split('+'))

    def __add__(self, other):
        sum_num = (list(map(sum, (zip(ComplexNumber.get_complex_num(self.complex_number),
                                      ComplexNumber.get_complex_num(other.complex_number))))))
        return ComplexNumber(f"{'+'.join(map(str, sum_num))}j")

    def __mul__(self, other):
        mul_num = (list(map(lambda x: x[0] * x[1], zip(ComplexNumber.get_complex_num(self.complex_number),
                                                       ComplexNumber.get_complex_num(other.complex_number)))))
        return ComplexNumber(f"{'+'.join(map(str, mul_num))}j")


a = ComplexNumber(10 + 12j)
b = ComplexNumber(2 + 2j)
print(a)
print(b)
c = a + b
print(c)
print(type(c))
d = a * b
print(d)
print(type(d))
