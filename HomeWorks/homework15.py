# Создать лямбда выражения для нахождения площадей фигур
import math

sq = {
    "circle": lambda r: print(f"Площадь окружности радиуса {r}: {math.pi*r**2}"),
    "rectangle": lambda width, height: print(f"Площадь прямоугольника размером {width}*{height}: {width*height}"),
    "trapeze": lambda a, b, h: print(f"Площадь трапеции для a={a}, b={b}, h={h}: {(a+b)/2*h}"),
}

sq["circle"](2)
sq["rectangle"](10, 15)
sq["trapeze"](7, 5, 3)
