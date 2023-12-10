# Написать функции, нахождения площади фигур
# 1 - прямоугольник, 2 - треугольник, 3 - круг

from math import pi


def rect(width, height):
    s = width * height
    return s


def triangle(height, base):
    s = 0.5 * base * height
    return s


def circle(radius):
    s = pi * radius**2
    return s


print("прямоугольник - 1, треугольник - 2, круг - 3")
change = input("Площадь какой фигуры вы хотите найти: ")

if change == str(1):
    w = int(input("Введите ширину прямоугольника: "))
    h = int(input("Введите высоту прямоугольника: "))
    s_rect = rect(w, h)
    print(f"Площадь прямоугольника: {s_rect}")
elif change == str(2):
    h = int(input("Введите высоту треугольника: "))
    b = int(input("Введите основание треугольника: "))
    s_triangle = triangle(h, b)
    print(f"Площадь треугольника: {s_triangle}")
elif change == str(3):
    r = int(input("Введите радиус круга: "))
    s_circle = circle(r)
    print(f"Площадь круга: {s_circle}")
else:
    print("Неправильный ввод данных")
