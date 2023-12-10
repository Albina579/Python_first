# Игра угадай число

import random

# number = 55
number = random.randint(1, 100)
n = int(input("Угадайте число от 1 до 100: "))
count = 1

if n == number:
    print("Вы угадали число с " + str(count) + " попытки")

while n != number:
    if n == 0:
        print("Вы вышли из игры")
        break
    elif n > number:
        print("Загаданное число меньше")
        n = int(input("Угадайте число от 1 до 100: "))
        count += 1
    elif n < number:
        print("Загаданное число больше")
        n = int(input("Угадайте число от 1 до 100: "))
        count += 1
    if n == number:
        print("Вы угадали число с " + str(count) + " попытки")
