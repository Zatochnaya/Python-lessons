--------------------------------------------------Задание 1------------------------------------

import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(lambda r: " ".join(map(str,r)), self.matrix)) + "\n"

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)


--------------------------------------------------Задание 2------------------------------------

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)

class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5

class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3

a = Coat(52)
b = Suit(1.80)
print(a)
print(a.expense)
print(b.expense)


--------------------------------------------------Задание 3------------------------------------

class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'number of cells - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1,count+1):
                print(self.simbol, end ='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end = '')


a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)