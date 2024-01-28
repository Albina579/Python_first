# Вычислить количество отрицательных чисел в массиве через рекурсию

def count_negative(lst):
    if len(lst) == 1:
        if lst[0] < 1:
            return 1
        else:
            return 0
    else:
        if lst[0] < 1:
            return 1 + count_negative(lst[1:])
        else:
            return count_negative(lst[1:])


print(f"Количество отрицательных чисел: {count_negative([-2, 3, 8, -11, -4, 6, -8, 5, -3])}")
