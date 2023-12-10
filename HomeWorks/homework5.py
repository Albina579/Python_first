# Найти среднее арифметическое всех ненулевых элементов введённого списка

count = 0  # количество ненулевых элементов списка
summa = 0  # сумма ненулевых элементов списка

arr = [int(input("-> ")) for i in range(int(input("Введите количество элементов: ")))]
print(f"Ваш список: {arr}")

for i in arr:
    if i != 0:
        summa += i
        count += 1

average = summa / count
print(f"Среднее арифметическое ненулевых элементов: {average}")


# Выведите все элементы списка с чётными индексами

array = [int(input("-> ")) for i in range(int(input("Введите количество элементов: ")))]
for i in range(len(array)):
    if i % 2 == 0:
        print(array[i], end=" ")
