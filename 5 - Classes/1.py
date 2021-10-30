from abc import abstractmethod, ABC
import math


class GeometricShape:
    @abstractmethod
    def square(self):
        """
        Calculate square of the shape
        :return:
        """
        pass

    def perimeter(self):
        """
        Calculate perimeter of the shape
        :return:
        """
        pass


class Quadrilateral(GeometricShape, ABC):
    angles = 4


class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        self.s_1 = a
        self.s_2 = b

    def square(self):
        return self.s_1*self.s_2

    def perimeter(self):
        return (self.s_1 + self.s_2) * 2


class Trapezoid(Quadrilateral):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def square(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        if a > b:
            s = (a + b) * (1 / 2) * math.sqrt(c ** 2 - (((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (b - a))) ** 2)
        else:
            s = (a + b) * (1 / 2) * math.sqrt(c ** 2 - (((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (a - b))) ** 2)
        s = round(s, 2)
        return s

    def perimeter(self):
        return self.a + self.b + self.c + self.d


class Parallelogramm(Quadrilateral):
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle * math.pi / 180

    def square(self):
        a = self.a
        b = self.b
        return round(a * b * math.sin(self.angle), 2)

    def perimeter(self):
        return (self.a + self.b) * 2


class Circle(GeometricShape):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return round((self.radius**2)*math.pi, 2)

    def perimeter(self):
        return round(2*math.pi*self.radius, 2)


Rec = Rectangle(3, 5)
Trap = Trapezoid(7, 4, 5, 6)
Par = Parallelogramm(4, 6, 60)
Cir = Circle(5)

shapes = []

shapes.append(Rec)
shapes.append(Trap)
shapes.append(Par)
shapes.append(Cir)

for shape in shapes:
    print(shape.square(), shape.perimeter())
