# Заполнить список уникальными случайными числами

import random

# s = [i for i in range(int(input("Введите количество уникальных целых чисел: ")))]
# random.shuffle(s)
# print(s)

arr = []
index = 0
k = int(input("Введите количество, не превышающее 10, уникальных целых чисел: "))
while len(arr) < k:
    r = random.randint(1, 10)
    if r not in arr:
        arr.append(r)
        index += 1
    else:
        r_new = random.randint(1, 10)
        while r_new == r:
            r_new = random.randint(1, 10)
        if r_new not in arr:
            arr.insert(index, r_new)
            index += 1
print(arr)
