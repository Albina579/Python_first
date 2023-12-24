# Пользователь вводит данные о количестве студентов: их фамилии, имена и баллы для каждого.
# Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего.

n = int(input("Введите количество студентов: "))
summa = 0
list_name = []
list_grade = []

for i in range(1, n+1):
    print(f"{i}-й студент")
    name = input("Имя: ")
    # surname = input("Фамилия: ")
    grade = int(input("Балл: "))
    summa += grade
    list_name.append(name)
    list_grade.append(grade)

dict_students = dict(zip(list_name, list_grade))
middle = summa / n

list_middle_more = []
for k in dict_students:
    if dict_students[k] > middle:
        list_middle_more.append(k)

print(f"Средний балл {middle}. Студенты с баллом выше среднего:")
print(*list_middle_more, sep='\n')
