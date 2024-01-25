# lesson 1
import re

# типизация данных: явная, динамическая, сильная (не можем сложить разные типы данных)
# print("HI!!!!!!!!!")
# print("Привет")
# name = "Пётр"  # инициализация переменной
# print("Hello,", name)
# age = 25
# print(age)
# age = "Hello"
# print(age)
# print(type(age))  # определение типа данных
# int - 20, float - 20.5, str - "Hello", bool - True (False)

# a = 4
# b = 5
# c = 1_111_111
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))
# переменная ссылается на ту ячейку памяти, в которой хранится значение

# a = b = c = 5 # множественное присваивание
# x, y, z = 5, "Hello", 5.7

# name_new = "Victor"

# PI = 3.14  # константа, её можно менять

# a = 1
# b = 4
# print("a:", a)
# print("b:", b)

# temp = a  # 1
# a = b
# b = temp

# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка \nсимволов')
# print('строка \nсимволов \'file.txt\'')
# print('строка \nсимволов \rfile.txt')
# print('строка \nсимволов D:\\folder\\file.txt')
# print("I like \"Monty Python\"")
# print("I like 'Monty Python'")
# print('I\'m Monty Python.')

# s1 = "Hi"
# s2 = "Python"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s1 + " " + s2 + "!")
# print(s1, s2, "!")
# print(s3 * 3)

# арифметические операторы
# print(9 + 6)
# print(9 - 1)
# print(9 * 5)
# print(9 ** 5)  # возведение в степень
# print(9 % 5)  # остаток от деления
# print(9 / 3)
# print(9 / 4)
# print(9 // 2)  # целочисленное деление

# print(.5)  # 0.5
# print(5e4)  # 50000.0
# print(5e-2)  # 0.05

# print(0o123)  # 8-я сс; 10-я сс 83
# print(0x123)  # 16-я сс; 10-я сс 291


# lesson 2

# num = 54321
# print("Исходное число: ", num)
# ost1 = num // 10000
# ost2 = num // 1000 % 10
# ost3 = num // 100 % 10
# ost4 = num // 10 % 10
# ost5 = num % 10
# res1 = ost5 * 10000 + ost4 * 1000 + ost3 * 100 + ost2 * 10 + ost1
# print(res1)

# res2 = num % 10 * 10000
# num //= 10
# res2 += num % 10 * 1000
# num //= 10
# res2 += num % 10 * 100
# num //= 10
# res2 += num % 10 * 10
# num //= 10
# res2 += num % 10
# print(res2)


# num1 = "2"
# num2 = 3
# res1 = num1 + str(num2)
# res2 = int(num1) + num2
# print(res1)
# print(res2)

# print(int(5.8))
# print(round(5.8))
# print(round(5.2))
# print(round(5.5783, 2))

# name = "Victor"
# age = 23
# print("My name is", name, ". I am", age, "years old.", sep="+")
# print("My name is" + name + ". I am " + str(age) + " years old.", end=" ")
# print("I learn Python")

# name = input("Введите ваше имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print(res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# False => "", 0, False, None

# print(7 == "7")
# print(5 + 2 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(8 <= 5)
# print(8 >= 5)
# print("привет" >= "ПРИВЕТ")

# print(2 < 4 < 9)
# print(2*5 > 7 >= 4+3)
# print(3*3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5-3 == 2 and 1+3 == 4)
# print(5-3 == 2 and 1+3 < 4)
# print(5-3 > 2 and 1+3 == 4)
# print(5-3 > 2 and 1+3 < 4)

# print(5-3 == 2 or 1+3 == 4)
# print(5-3 == 2 or 1+3 < 4)
# print(5-3 > 2 or 1+3 == 4)
# print(5-3 > 2 or 1+3 < 4)

# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = int(input("Введите первую сторону треугольника: "))
# b = int(input("Введите вторую сторону треугольника: "))
# c = int(input("Введите третью сторону треугольника: "))
# if a == b == c:
#     print("равносторонний")
# elif a == b or a == c or b == c:
#     print("равнобедренный")
# else:
#     print("разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("monday")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# lesson 3

# pass - ключевое слово для загрузки пустого блока кода, аналог ...

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# аналог switch
# day = 'friday'
# time = 17
# match day:
#     case 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday' if 9 <= time <= 16:
#         print("day work")
#     case 'saturday' | 'sunday':
#         print("weekend")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 10, 20
# print(a if a < b else b)  # тернарное выражение

# a, b = 10, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 10, 0
# print(f"a / b = {a / b}" if b != 0 else "На 0 делить нельзя")

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
# print("следующая строка")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("нельзя делить на 0")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")
# else:  # когда в блоке try не возникли исключения
#     print(f"Всё хорошо! Вы ввели числа: {n} и {m}")
# finally:  # выполнится в любом случае
#     print("program's end")

# n1 = input("Введите первое число: ")
# n2 = input("Введите второе число: ")
# try:
#     n1 = int(n1)
#     n2 = int(n2)
# except ValueError:
#     n1 = str(n1)
# finally:
#     print(n1 + n2)

# i = 2
# while i <= 20:
#     print(f"i = {i}")
#     i += 2

# count = int(input("Введите количество символов: "))
# while count > 0:
#     print("*", end="")
#     count -= 1

# count = int(input("Введите количество символов: "))
# print("*" * count)

# a = int(input("Введите начала диапазона: "))
# b = int(input("Введите конец диапазона: "))
# summa = 0
# while a <= b:
#     if a % 2:   # a%2!=0
#         summa += a
#     a += 1
# print(summa)


# lesson 4

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("нецелое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён")

# i = 0
# while True:
#     print(i)
#     if i == 7:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите числа: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("Внутренний цикл: i =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(f"{i} * {j} = {i * j}", end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# for i in "Hello", "world", "!":
#     print(i)

# for i in range(2, 20, 5):
#     print(i, end=" ")

# for j in range(15, 5, -1):
#     print(j, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i)


# lesson 5

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++ i =", i)
#     for j in range(2):
#         print("--- j =", j)

# row = 4
# col = 12
# for i in range(row):
#     for j in range(col):
#         print("*", end="")
#     print()

# row = int(input("Введите высоту прямоугольника: "))
# col = int(input("Введите ширину прямоугольника: "))
# for i in range(row):
#     for j in range(col):
#         if i == 0 or i == row-1 or j == 0 or j == col - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter * 2 for letter in "Banana"]
# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# nums = [5, 7, 3, "cat", True]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[-1])
# nums[2] = 256
# print(nums)
# nums[3] *= 3
# print(nums)
# print(len(nums))  # длина списка
# for i in range(len(nums)):
#     print(f"{i} - {nums[i]}")

# пустые списки
# arr1 = []
# arr2 = list()

# arr = list("hello")  # преобразование в список
# print(arr)

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10, 2)))

# a = [i for i in range(5)]
# print(a)
# a = [0 for _ in range(5)]
# print(a)

# n = 5
# b = [i**2 for i in range(1, n+1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 5
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# summa = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         summa += a[i]
# print(summa)

# a = list(range(10, 100, 25))
# print(a)
# for i in range(len(a)):
#     print(f"i = {i}: {a[i] + 5}")
# print()
# for i in a:
#     print(i+7, end=" ")

# summa = 0
# count = 0
# n = list(range(21, 41))
# for i in range(len(n)):
#     if n[i] % 2 != 0:
#         summa += n[i]
#     else:
#         count += 1
# print(f"сумма нечётных элементов: {summa}, количество чётных элементов: {count}")
#
# for i in n:
#     if i % 2 != 0:
#         summa += i
#     else:
#         count += 1
# print(f"количество чётных элементов: {count}, сумма нечётных элементов: {summa}")

# n = [int(input("-> ")) for i in range(int(input("Введите количество символов = ")))]
# print(n)
# for i in range(1, len(n)):
#     if n[i] > n[i-1]:
#         print(n[i])


# lesson 6

# срезы
# a = [7, 8, 2, 32, 19, 5, 249]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# print(a[1:4])  # срез
# print(a[1:])
# print((a[:3]))
# print(a[::-1])

# arr = list(range(1, 8))
# print(arr)
# print(arr[::-1])
# print(arr[::2])
# print(arr[1::2])
# print(arr[:1])
# print(arr[-1:])
# print(arr[3:4])
# print(arr[-3:])
# print(arr[-3:1:-1])
# print(arr[2:5])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[4:] = []
# print(s)
# del s[1]
# print(s)
# del s[2:5]
# print(s)

# методы списка
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (2-й параметр) в заданный индекс (1-й параметр)
# print(s)
# s.remove(9)  # удаляет первый элемент по заданному значению
# print(s)
# s.pop()  # удаляет последний элемент
# print(s)
# a = s.pop(1)  # передаём индекс для удаления элемента
# s.clear()  # очистка всех элементов списка
# print(s)

# s = []
# n = int(input("Введите количество элементов: "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input("Введите количество элементов: "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 != 0:
#         print(f"{x} - не делится на 3 без остатка")
#     else:
#         s.append(x)
# print(s)

# a = [5, 9, 3, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append((b[i]))
# print(c)
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append((b[i]))
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append((a[i]))
# print(c)

# s = []
# n = int(input("Введите количество элементов: "))
# for i in range(n):
#     x = int(input("Введите число: "))
# k = int(input("Введите индекс удаляемого элемента: "))
# s.pop(k)
# print(s)

# s = [9, 2, 5, 9, 4, 3, 9]
# print(s)
# num = s.count(9)
# print(num)
# ind = s.index(9)  # возвращает индекс первого искомого элемента
# print(ind)
# ind1 = s.index(9, 2)
# print(ind1)


# lesson 7

# методы списка
# a = [1, 2, 3]
# b = a
# print("a = ", a)
# print("b = ", b)
# a.append(20)
# print("a = ", a)
# print("b = ", b)
# b.append(30)
# print("a = ", a)
# print("b = ", b)

# a = [1, 2, 3]
# b = a.copy()
# print("a = ", a)
# print("b = ", b)
# a.append(20)
# print("a = ", a)
# print("b = ", b)
# b.append(30)
# print("a = ", a)
# print("b = ", b)

# a = [1, 2, 3, 9, 5, 4]
# print(a)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort()  # сортирует элементы списка, изменяя его, но не возвращая его
# print(a)
# a.sort(reverse=True)  # сортирует элементы списка в обратном порядке
# print(a)

# b = ['Виталий', "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# sort = sorted(a)  # возвращает, создаёт новый список, не меняя исходный
# print(sort)


# import random
# print(random.random())
# print(random.randint(0, 9))  # От 3 до 9 включительно целые числа
# print(random.randrange(3, 9, 2))  # от 3 до 9 не включительно
# print(round(random.uniform(10.5, 25.5), 2))

# city = ["Москва", "Санкт-Петербург", "Лондон", "Париж", "Стокгольм"]
# print((random.choice(city)))
# print((random.choices(city, k=2)))
# random.shuffle(city)
# print(city)

# s = [55, 77, 88, 99, 3, 6, 8, 89, 9, 3, 45, 0, 21]
# print(random.choice(s))
# print(random.choices(s, k=3))


# let = [5, 4, 8, 9, 1]
# print("Количество элементов:", len(let))
# print("Сумма элементов:", sum(let))
# print("Минимум:", min(let))
# print("Максимум:", max(let))


# import random
# arr = [random.randint(0, 100) for i in range(10)]
# print(arr)
# m = max(arr)
# print(f"MAX: {m}")
# arr.remove(m)
# arr.insert(0, m)
# print(arr)

# import random
# arr = [random.randint(0, 100) for i in range(10)]
# print(arr)
# m = min(arr)
# print(f"min: {m}")
# ind_m = arr.index(m)
#
# del arr[:ind_m]
# print(arr)
#
# print(arr[ind_m:])


# x = list("12ieh84kj32")
# print(x)
# print("k" in x)
# print("a" in x)
# print("k" not in x)
# print("a" not in x)


# arr = []
# if len(arr) == 0:
# if not arr:
#     print("Пусто")
# else:
#     print("Что-то есть")

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
#
# print("Первый список", a)
# print("Второй список", b)
#
# c = a + b
# print(c)
#
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in b:
#         d.append(element)
# print("Элементы обоих списков без повторений: ", d)
#
# e = []
# for i in a:
#     if i in b and i not in e:
#         e.append(i)
# print("Элементы общие для двух списков: ", e)
#
# f = [min(a), min(b), max(a), max(b)]
# print(f)

# m = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13]
# ]
# m = ["Hello", "world", "!"]
# print(m)
# print(len(m))
# print(m[1][2])  # m[row][col]
# print()
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
# for row in m:
#     for col in row:
#         print(col, end='\t')
#     print()


# lesson 8

# w, h = 4, 3
#
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
#
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import random
# w, h = 4, 3
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
#
# count = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             count += 1
#     print()
# print(f"Количество отрицательных элементов: {count}")

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x+y)

# w, h = 4, 3
# matrix = [[input("-> ") for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import math
# num1 = math.sqrt(2)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
# print(math.pi)

# import math as m
# n = m.sqrt(4)

# from math import sqrt, ceil
# print(sqrt(2), ceil(5.7))

# from math import *

# import locale
# import time
# seconds = time.time()
# print("количество секунд:", seconds)
#
# local_time = time.ctime(192874)
# print("местное время:", local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("Сегодня: %B %d, %Y"))
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S"))
#
# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# Функция
# def hello(name):  # аргументы
#     print("HELLO", name)
#
#
# hello("Irina")  # параметры
# hello("Igor")

# def get_sum(a, b):
#     return a+b
#
#
# a1 = 2
# b1 = 3
# res = get_sum(a1, b1)
# print(res)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "x", "0")

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 15))

# def diff(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x = int(input("Введите первое число: "))
# y = int(input("Введите второе число: "))
# print(diff(x, y))

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе равно =", cube(i))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#
#     # symbol1 = lst.pop(0)
#     # symbol2 = lst.pop()
#     # lst.append(symbol1)
#     # lst.insert(0, symbol2)
#
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 10
# b = 5
# print(is_greater(a, b))
# print(is_greater(5, 10))
#
# if is_greater(a, b):
#     print(a, ">", b)
# else:
#     print(b, ">", a)

# def check_pass(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_pass(p):
#     print("Надёжный пароль")
# else:
#     print("Ненадёжный пароль")


# lesson 9

# def get_sum(a, b, c=5, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=7))

# def set_param(count=20, s="-"):
#     print(s * count)
#
#
# set_param()
# set_param(7)
# set_param(5, "*")
# set_param(s="#")

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Сумма чётных цифр")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечётных цифр")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

# Изменяемый тип данных - только списки: адрес в памяти не изменяется при изменении самого списка
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# n = 5
# m = 5
# print(n is m)

# кортеж (tuple) - неизменяемый тип данных - любая последовательность элементов
# lst = [10, 20, 30]  # список
# tpl = (10, 20, 30)  # кортеж
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
# print(a)
# print(b)

# a = 5, 9, 1, 3, 8  # кортеж
# print(a)
# print(type(a))
# b = (5,)
# c = 5,

# n = [1, 2, 3]
# b = tuple(n)
# print(type(b))
# print(b)

# c = tuple("Hello")
# print(type(c))
# print(c)

# n = "hello", "python"
# b = tuple(n)
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[3])
# print(a[1:3])

# s = [i for i in range(5)]
# print(s)

# import random
# s = tuple(input("-> ") for i in range(5))
# s = tuple(random.randint(1, 50) for i in range(5))
# print(s)

# s = tuple(2**i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t1 * 2)
# print(t3.count("l"))
# if "l" in t3:
#     print(t3.index("l"))
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             a = tpl.index(el)
#             b = tpl.index(el, a+1)
#             return tpl[a:b+1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, year, married = get_user()
# print(first_name, year, married)


# lesson 10

# tpl = (1, 3, 4, 5, 5, 7)
# print(tpl)
#
# lst = list(tpl)
# print(lst)
#
# ptl1 = tuple(lst)
# print(ptl1)

# countries = (
#     ("England", 80.5, (("London", 4.29), ("Briton", 2.39))),
#     ("France", 80, (("Parish", 8.3), ("Marcel", 4.8))),
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, 'население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print(f"\tГород: {city_name}, население = {city_population}")

# print("Вносим изменения")


# lesson 11

# множество (set) - неупорядоченный коллекционный тип данных, хранящий уникальные элементы

# s = {"banana", "apple", "orange"}
# print(s)

# a = set()  # пустое множество

# c = ["red", "blue", "green", "red"]
# a = set(c)
# print(a, type(a))

# s = {x for x in range(10)}
# print(s)

# s = {x * x for x in range(10)}
# print(s)

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas if x % 2 == 0}
# print(s)

# def to_set(elem):
#     st = set(elem)
#     return st, len(st)
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# print("green" in t)
# print("green" not in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = [i for i in r if "a" in i]
# a = {"A"+i[1:] if i[0] == "a" else "B"+i[1:] for i in r}
# a = {"A"+i[1:] if i[0] == "a" else "B"+i[1:] for i in r if i[1] == "c"}
# print(a)

# a = {"tom", "bob", "alice"}
# print(a)
# a.add("ann")
# print(a)
# a.remove("tom")  # если нет удаляемого элемента, выбрасывает ошибку
# print(a)
# user = "bob"
# if user in a:
#     a.remove(user)
# print(a)
# a.discard("ann")  # если нет удаляемого элемента, не выбрасывает ошибку
# print(a)
# n = a.pop()  # удаляет первый элемент
# print(n)
# print(a)
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b  # или
# print(c)
# a |= b
# print(a)
# d = a & b  # и
# print(d)
# a &= b
# print(a)
# e = a - b
# print(e)
# a -= b
# print(a)
# f = a ^ b  # симметричная разность {0, 4}
# print(f)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(f"Уникальные элементы: {s}")
# c = len(s)
# print(f"Уникальные элементы, количество: {c}")
# print(f"min {min(s)}")
# print(f"max {max(s)}")
# print(f"sum {sum(s)}")

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# for i in a:
#     print(i)
# print(*a)

# drawing = {"марина", "женя", "света"}
# music = {"костя", "женя", "илья"}
# one_hobby = drawing ^ music
# print(f"Only one hobby: {one_hobby}")
# both_hobbies = drawing & music
# print(f"Both hobbies: {both_hobbies}")
# drawing -= both_hobbies
# print(f"drawing: {drawing}")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)  # a подмножество b
# print(b <= a)  # b подмножество a

# s = frozenset([1, 2, 3, 4, 5])  # неизменяемый set
# print(type(s))
# print(s)
# a = frozenset({"hello", "world"})
# print(a)

# a = [8, 9, 7, 4, 5, 8, 7, 9, 6, 4, 6, 5, 1, 2, 4, 5]
# print(a)
# b = set(a)
# a = list(b)
# print(a)


# lesson 12

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3, 4: "four"}  # словарь
# print(lst[0])
# print(d["one"])
# lst[0] = 10
# d["one"] = 10
# print(d[4])

# d = {}
# print(d)
# print(type(d))
# d1 = dict()

# d = dict({"one": 1, "two": 2, "three": 3, 4: "four"})
# d = dict(one=1, two=2, three=3, four="four")

# ключами в словаре могут быть только неизменяемые типы данных
# d = {0: 1, "two": 2, (1, 2.3): "кортеж", True: [2, 3, 4, 6]}
# print(d)

# d = {0: 1, "two": 2, (1, 2.3): "кортеж", True: [2, 3, 4, 6]}
# print(d[True][1])
# print(d[(1, 2.3)])
# print(d["two"])
# print(d[0])

# lst = [["one", 1], ["two", 2], ["three", 3]]
# d = dict(lst)
# print(d)

# d = {a: a**2 for a in range(7)}
# print(d)

# d = {"one": 1, "two": 2, "four": 4}
# if "one" in d:
#     print("TRUE")
# print("one1" in d)
# key = "four"
# if key in d:
#     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + "нет в словаре")
# for i in d:
#     print(i, ":", d[i])

# m = 1
# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# for i in d:
#     m *= d[i]
# print(m)

# d = dict()
# d[1] = input("Введите что-нибудь")
# d[2] = input("Введите что-нибудь")
# d[3] = input("Введите что-нибудь")
# d[4] = input("Введите что-нибудь")
# d = {i: input("Введите что-нибудь") for i in range(1, 5)}
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# print(len(d))
# print(max(d))
# d = {3: "x1", 7: "x2", 5: "x3", -1: "x4"}
# print(sum(d))

# goods = {
#     '1': ['Core-i34330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
# for i in goods:
#     print(f"{i}) {goods[i][0]} - {goods[i][1]} шт. по {goods[i][2]}руб")
#
# while True:
#     n = input("Введите номер товара: ")
#     if n != "0":
#         count = int(input("Введите количество товаров: "))
#         try:
#             goods[n][1] += count
#         except KeyError:
#             pass
#     else:
#         break
#
# for i in goods:
#     print(f"{i}) {goods[i][0]} - {goods[i][1]} шт. по {goods[i][2]}руб")

# методы работы со словарём
# d = {"a": 1, "b": 2, "c": 3}
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений в виде кортежа
# for key in d:
#     print(key, "->", d[key])
# for key in d.keys():
#     print(key)
# for value in d.values():
#     print(value)
# for key, value in d.items():
#     print(key, "->", value)
#
# print(list(d))
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
# print(tuple(d.items()))
#
# d2 = d
# print(f"d: {d}, id = {id(d)}")
# print(f"d2: {d2} id = {id(d2)}")
# d2['a'] = 5
# d['e'] = 7
# print(f"d: {d}, id = {id(d)}")
# print(f"d2: {d2} id = {id(d2)}")
#
# d2 = d.copy()  # копирует и создаёт новый словарь
# print(f"d: {d}, id = {id(d)}")
# print(f"d2: {d2} id = {id(d2)}")
# d2['a'] = 5
# d['e'] = 7
# print(f"d: {d}, id = {id(d)}")
# print(f"d2: {d2} id = {id(d2)}")
#
# d.clear()  # очищает словарь, оставляя пустой словарь
#
# print(d['b'])
# print(d['e'])  # выдаст ошибку
# val1 = d.get("b", "Такого ключа не существует")
# val2 = d.get("e", "Такого ключа не существует")
# print(val1)
# print(val2)
#
# item1 = d.pop('b', "Такого ключа не существует")
# print(item1)
# print(d)
#
# item2 = d.pop('e', "Такого ключа не существует")
# print(item2)
# print(d)
#
# item3 = d. popitem()  # удаляет последний элемент
# print(item3)
# print(d)


# lesson 13

# d = {"a": 1, "c": 3, "b": 2}
#
# d1 = {"r": 7, "q": 40}
#
# d.update(d1)
# print(d)
#
# # d2 = {"a": 20, "b": 9}
# d2 = [("a", 20), ("b", 9)]
# d.update(d2)
# print(d)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# # z = {}
# # z.update(x)
# # z.update(y)
# z = x | y  # объединение словарей
# print(z)

# a = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three",
#     },
#     "second": {
#         4: "four",
#         5: "five",
#     }
# }
# print(a)
# for i in a:
#     print(i)
#     for j in a[i]:
#         print("\t", j, " : ", a[i][j], sep="")

# sales = {
#     "John": {
#         "N": 3056,
#         "S": 8463,
#         "E": 8441,
#         "W": 2694,
#     },
#     "Tom": {
#         "N": 4832,
#         "S": 6786,
#         "E": 4737,
#         "W": 3612,
#     },
#     "Ane": {
#         "N": 5239,
#         "S": 4802,
#         "E": 5820,
#         "W": 1859,
#     },
#     "Fiona": {
#         "N": 3904,
#         "S": 3645,
#         "E": 8821,
#         "W": 2451,
#     },
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep='')
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# d = {value: key for key, value in d.items()}
# print(d)

# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = {}
# current_key = ""
# for item in a:
#     if type(item) == str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
# print(d)

# d = dict(zip([1, 2, 3], ["one", "two", "three"]))  # объединяет
# print(d)
#
# a = [1, 2, 3]
# b = ["one", "two", "three"]
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = [1, 2, 3]
# b = ["one", "two", "three"]
# q = [4.5, 4.9, 1.8]
# c = tuple(zip(a, b, q))
# p = list(zip(a, b, q))
# s = set(zip(a, b, q))
# d = dict(zip(a, b))
# print(c, p, s, d, sep="\n")

# d_one = {"name": "Igor", "last_name": "Petrov", "job": "Consultant"}
# d_two = {"name": "Irina", "last_name": "Petrova", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# d = [(1, "one"), (2, "two"), (3, "three")]
# a, b = zip(*d)  # распаковывает
# print(a, b, sep="\n")

# a = ["two", "one", "three"]
# b = [3, 2, 1]
# d = list(zip(a, b))
# d.sort()
# print(d)
# print(dict(d))
# s = sorted(d.items())

# one = {"apple": 0.45, "orange": 0.7}
# two = {"pepper": 0.1, "onion": 0.55}
# print({**one, **two})
# for k, v in {**two, **one}.items():
#     print(k, "->", v)

# data = ["red", "green", "blue"]
# num = 1
# for v in data:
#     print(num, ") ", v, sep="")
#     num += 1
# print()
# for n, v in enumerate(data, 1):
#     print(n, ") ", v, sep="")


# lesson 14

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]  # * распаковывает
# print(b)

# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))

# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))

# def func(*args):
#     middle = sum(args) / len(args)
#     print(middle)
#     res = []
#     for element in args:
#         if element < middle:
#             res.append(element)
#     return res
#
#
# first = func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(first)
# second = func(3, 6, 1, 9, 5)
# print(second)

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 5, 6, 7))

# def print_score(student, *scores):
#     print(f"Student Name {student}")
#     for score in scores:
#         print(score)
#
#
# print_score("Irina", 5, 4, 2, 3, 4, 4)
# print_score("Petr", 4, 2, 4, 5, 3)
# print_score("Lev")

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "->", v)
#     print()
#
#
# intro(name="Irina", surname="Black", age=22)
# intro(name="Igor", surname="Petrov", email="igor@gmail.com", age=22, phone="+70910958388")

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# print(my_dict)

# def func(a,  *args, d, **kwargs):
#     return a, d, args, kwargs
#
#
# # print(func(5))  # чтобы сработало, убрать нужно d
# print(func(5, 9, 2, 35, 643, k1=22, k2=32, k3=9, d=55))

# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     # global name
#     name = "Sam"  # локальная переменная
#     surname = "Black"  # локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Bye", name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# def add_five(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#
#     return add_some()
#
#
# print(add_five(5))


# lesson 15

# def outer(who):
#     def inner():
#         print("Hello", who)
#     inner()
#
#
# outer("world")

# def fun1():
#     a = 5
#
#     def fun2(b):
#         a = 9
#         print(a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# def fn1():
#     x = 25  # 2
#
#     def fn2():
#         x = 33  # 4
#
#         def fn3():
#             nonlocal x  # переменная на уровень выше
#             x = 55  # 6
#
#         fn3()  # 5
#         print("fn2, x =", x)  # 7
#
#     fn2()  # 3
#     print("fn1, x =", x)  # 8
#
#
# fn1()  # 1

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# Замыкание
# def outer(n):
#     def inner(x):
#         return n+x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item2(2))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b += "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Moscow")
# res1()
# res1()
# res2 = func("Sochi")
# res2()
# res2()
# res2()
# res1()

# анонимные функции lambda
# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))

# print((lambda x, y: x**2 + y**2)(2, 5))
# print((lambda x, y=5: x**2 + y**2)(2, 10))
# print((lambda x=3, y=5: x**2 + y**2)(2, 10))

# print((lambda *args: args)(1, 2, 3, 4, 5))

# y = (
#     lambda x: x*2,
#     lambda x: x*3,
#     lambda x: x*4,
# )
#
# for i in y:
#     print(i("abc__"))

# def outer(n):
#     def inner(x):
#         return x+n
#     return inner
#
#
# f = outer(5)
# print(f(10))


# def outer1(n):
#     return lambda x: x+n
#
#
# f1 = outer1(5)
# print(f1(10))

# outer2 = lambda n: lambda x: x + n
# f2 = outer2(5)
# print(f2(10))

# print((lambda n: lambda x: x + n)(5)(10))

# print((lambda x: lambda y: lambda z: x+y+z)(2)(4)(6))

# d = {"b": 3, "c": 1, "a": 2}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d1 = dict(lst)
# print(d1)

# players = [
#     {"name": "Антон", "lastname": "Бирюков", "rating": 9},
#     {"name": "Алексей", "lastname": "Бодня", "rating": 10},
#     {"name": "Фёдор", "lastname": "Сидоров", "rating": 4},
#     {"name": "Михаил", "lastname": "Семёнов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda item: item["lastname"])
# print(res)
#
# res2 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res2)

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
# ]
#
# print(a[0](5, 2))
# print(a[1](5, 2))
# print(a[2](5, 2))
# print(a[3](5, 2))

# d = {
#     1: lambda: print("Monday"),
#     2: lambda: print("Tuesday"),
#     3: lambda: print("Wednesday"),
#     4: lambda: print("Thursday"),
#     5: lambda: print("Friday"),
#     6: lambda: print("Saturday"),
#     7: lambda: print("Sunday"),
# }
#
# d[6]()

# print((lambda a, b: a if a > b else b)(15, 13))

# print((lambda a, b, c: a if a < b < c else (b if b < c else c))(15, 13, 14))


# lesson 16

# def mult(t):
#     return t * 2
#
#
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst1))
# print(lst2)

# lst1 = [2, 8, 12, -5, -10]
# lst2 = list(map(lambda t: t*2, lst1))
# print(lst2)

# t = (2.88, -1.75, 100.55)
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# st = ["a", "b", "c", "d", "e"]
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# num = ["1", "2", "3", "4", "5"]
# res = list(map(int, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: x+y, l1, l2))
# print(res)

# t = ("abcd", "abc", "asdfq", "def", "grt")
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 78, 997, 32, 68, 88, 71, 90]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
# n = [x ** 2 for x in range(10) if x % 2]
# print(n)

# import random
# lst = [random.randint(1, 40) for i in range(20)]
# print(lst)
# res = list(filter(lambda num: 10 <= num <= 20, lst))
# print(res)

# def hello():
#     return "hello I am func 'hello'"
#
#
# def supper_func(func):
#     print("hello I am func 'supper_hello'")
#     print(func())
#
#
# supper_func(hello)

# def hello():
#     return "hello I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#     return wrap
#
#
# def func_test():
#     print("hi I am fun 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print("*" * 30)
#         func()
#         print("=" * 30)
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("hi I am fun 'func_test'")
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap(arg1, arg2):
#         nonlocal count
#         count += 1
#         fn(arg1, arg2)
#         print("Вызов функции:", count, "\n", "*" * 20, sep="")
#     return wrap
#
#
# @cnt
# def hello(a, b):
#     print("Hello", a, "\nHello", b)
#
#
# hello("Python", "JS")
# hello("one", "two")
# hello(5, 10)

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "learn", study, "\n")
#
#
# print_data("Boris", "Liza", "Sveta", study="JS")
# print_data("Vlad", "Kate", "Victor")

# def decor(args1, args2):
#     def args_decor(fn):
#         def wrap(x, y):
#             print(f"{args1} {x} {args2} {y} = ", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_decor
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(100, 45)

# def multiply(arg):
#     def args_decor(fn):
#         def wrap(num):
#             return fn(num) * arg
#         return wrap
#     return args_decor
#
#
# @multiply(3)
# def func(num):
#     return num
#
#
# print(func(5))


# lesson 17

# print(int("100", 2))  # 4
# print(int("100", 8))  # 64
# print(int("100", 10))  # 100
# print(int("100", 16))  # 256
#
# print(bin(18))
# print(oct(18))
# print(hex(18))
#
# print(0b10110)
# print(0o173)
# print(0x1948A)
# print(0b1010 + 0o22 + 0x12 + 18)

# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print(e[1])
# print(e[-1])
# print(e[1:4])
# print(e[::-1])
# e = e[:3] + 't' + e[4:]
# print(e)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = changeCharToStr(str1, "N", "P")
# print(str1)
# print(str2)

# print("Привет")
# print(u"Привет")  # Unicode

# print(r"C:\folder\file.txt\\"[:-1])  # подавление экранирования
# print(r"C:\folder\file.txt" + "\\")  # подавление экранирования
# print("C:\\folder\\file.txt\\")

# name = "Dmitri"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет")
# m = 2.38707562
# print(f"Number {round(m, 2)}")
# print(f"Number {m:.2f}")

# x = 10
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x} * {y} / 2 = {x * y / 2}")

# num = 7
# print(f"{{{num}}}")
# print(f"{{{{{num}}}}}")

# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")

# """
# Многострочный
# текст
# """
#
# s = '''
# Многострочный
# текст
# '''
# print(s)

# def sq(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(sq(5))
# print(sq.__doc__)
# print(print.__doc__)
# print(sum.__doc__)

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# print(ord("a"))  # 97 - код символа
# print(ord("й"))  # 1081 - код символа

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# s = "Test string for me "
# arr = [ord(x) for x in s]
# print("ASCII codes:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))  # a


# lesson 18

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.count("h"))
# print(s.count("h", 1))
# print(s.find("l"))
# print(s.rfind("l"))
# print(s.index("l"))
# print(s.rindex("l"))

# s = input("Введите 2 слова через пробел: ")
# first = s[:s.find(" ")]
# second = s[s.find(" ")+1:]
# print(f"{second} {first}")

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello", 3))
# print(s.endswith("on."))
# print(s.endswith("lo", 3, 5))

# print("abc123".isalpha())
# print("abcABC".isalpha())
# print("123".isdigit())
# print("123.234".isdigit())
# print("123abc".isalnum())
# print("123Aabc".isalnum())
# print("abc".islower())
# print("ABC9".isupper())

# print("  py".lstrip())
# print("py   ".rstrip())
# print("    py   ".strip())

# print("https://www.python.org".lstrip())
# print("https://www.python.org".lstrip("/:pths").rstrip(".org"))
# print("https://www.python.org".strip("/:pths.org"))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1)
# print(str1.replace("Nython", "Python"))

# s1 = "-"
# seq = ("a", "b", "c")
# print(s1.join(seq))
#
# print("..".join(["1", "2"]))
# print(":".join("Hello"))

# s = "hello, WORLD! I am learning Python."
# print(s.split())
#
# print("www.python.org".split("."))

# a = input("-> ").split()
# print(a[0], a[1][0] + ".", a[2][0] + ".")

# a = input("Введите коды символов через пробел: ").split()
# print(a)
#
# b = list(map((int, a)))
# print(b)

# import re
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с шаблоном регулярного вырвжения
# print(re.search(reg, s))  # возвращает месторасположение первого совпадения с шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))  # возвращает месторасположение первого совпадения с шаблоном только в начале строки
# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "!", s))  # поиск и замена

# import re
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 189274 Hello[-World]"
# # reg = r"[204]"
# # reg = r"[0-9]"
# # reg = r"[12][0-9][0-9][0-9]"
# # reg = r"[А-яёЁ]"
# reg = r"[^А-яёЁ]"
# reg = r"[a-zA-Z\[\]-]"
# reg = r"[.]"   //  "\."
# reg = r"[\w]"  // поиск букв и английских и русских;  [\W] - инвертирует
# reg = r"[\w+]"
# reg = r"[\d]"  // поиск только цифр:  [\D] - инвертирует
# reg = r"[\d+]"
# reg = r"[\s]"  // поиск пробельных символов;  [\S] - инвертирует
# reg = r"[\AЯ ищу]"  // поиск в начале строки
# reg = r"[World]\Z]"  // поиск в конце строки
# reg = r"[году\b]"  // поиск слова
# print(re.findall(reg, s))
# reg = r"[\d{4}]"  // 4 повторений
# reg = r"[\d{4,8}]"  // от 4 до 8 повторений
# reg = r"[\d{4,}]"  // не менее 4 повторений
# reg = r"[\d{,8}]"  // не более 8 повторений
# reg = r"\w*"  // 0 или более
# reg = r"\w?"  // 0 или 1 вхождение
# reg = r"\w+"  // 1 или более


# lesson 19

# import re
# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:45. Минуты в диапазоне от 00 до 59. 2021-06-15Т01:09."
# reg = r"[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, s))

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"#.*", "", s))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub('-', '.', re.sub(r"#.*", "", s)))

# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# reg = r"\w+\s*=\s*[^;]+"
# print(re.findall(reg, s))

# s = "12 сентября 2021 года 235"
# reg = r"\d{2,4}"
# reg = r"\d{2,}"
# reg = r"\d{,4}"
# print(re.findall(reg, s))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 189274 Hello[-World] 5378 97648"
# reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# import re
#
#
# def valid_login(name):
#     return re.findall(r"^[A-Za-z0-9_-]{6,16}$", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python!!!"))
# print(valid_login("Python!!!Python"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w+", text, re.DEBUG))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"я"
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall(r"""
# [a-z.-]+
# @
# [a-z.-]+
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# lesson 20
