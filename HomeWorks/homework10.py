# Выведите статистику частотности символов в кортеже

s = input("Введите по порядку, без пробелов, элементы кортежа: ")
tpl = tuple(s)
print(tpl)
if "0" in tpl:
    print(f"Количество 0 = {tpl.count('0')}")
if "1" in tpl:
    print(f"Количество 1 = {tpl.count('1')}")
if "2" in tpl:
    print(f"Количество 2 = {tpl.count('2')}")
if "3" in tpl:
    print(f"Количество 3 = {tpl.count('3')}")
if "4" in tpl:
    print(f"Количество 4 = {tpl.count('4')}")
if "5" in tpl:
    print(f"Количество 5 = {tpl.count('5')}")
if "6" in tpl:
    print(f"Количество 6 = {tpl.count('6')}")
if "7" in tpl:
    print(f"Количество 7 = {tpl.count('7')}")
if "8" in tpl:
    print(f"Количество 8 = {tpl.count('8')}")
if "9" in tpl:
    print(f"Количество 9 = {tpl.count('9')}")
