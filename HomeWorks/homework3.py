# программа выводит на экран линию из символов
# пользователь указывает число символов, тип символа, ориентацию линии

count = int(input("Введите количество символов: "))
type_sign = input("Введите тип символа: ")
print("0 - горизонтальная \n1 - вертикальная")
orientation_line = int(input("Введите ориентацию линии: "))

if orientation_line != 0 and orientation_line != 1:
    print("Некорректно введена ориентация линии")

while count > 0:
    count -= 1
    if orientation_line == 0:
        print(type_sign, end="")
    elif orientation_line == 1:
        print(type_sign)
