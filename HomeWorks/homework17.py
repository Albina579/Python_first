# Вывести все символы, ASCII-коды, которые лежат между a и b включительно, в порядке возрастания их кодов

print("Введите диапазон")
a = int(input("от: "))
b = int(input("до: "))

if a > b:
    arr = [chr(i) for i in range(a, b-1, -1)]
    arr.sort()
    print(*arr)
else:
    for i in range(a, b+1):
        print(chr(i), end=" ")
