# Создать функцию, которая находит сумму любого количества чисел.
# Декоратор, который будет находить среднее арифметическое этих чисел

def decorator(fn):
    def wrap(*args):
        middle = fn(*args) / len(args)
        print("Среднее арифметическое чисел:", middle)
    return wrap


@decorator
def func_sum(*args):
    summa = sum(args)
    print("Сумма чисел:", summa)
    return summa


func_sum(2, 3, 3, 4)
