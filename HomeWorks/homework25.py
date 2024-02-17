from math import sqrt


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_size(self):
        print(f"Длина прямоугольника: {self.length}\nШирина прямоугольника: {self.width}")

    def calculate_square(self):
        return self.length * self.width

    def calculate_perimetr(self):
        return 2 * self.length + 2 * self.width

    def calculate_hypotenuse(self):
        return sqrt(self.length**2 + self.width**2)

    def draw_rectangle(self):
        for i in range(self.length):
            for j in range(self.width):
                print("*", end="")
            print()


r1 = Rectangle(3, 9)
r1.print_size()
s1 = r1.calculate_square()
print(f"Площадь прямоугольника: {s1}")
p1 = r1.calculate_perimetr()
print(f"Периметр прямоугольника: {p1}")
h1 = r1.calculate_hypotenuse()
print(f"Гипотенуза прямоугольника: {h1}")
r1.draw_rectangle()
