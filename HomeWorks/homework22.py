# обмен местами двух строк в файле

file_name = "homework22.txt"

with open(file_name, "w+") as f:
    f.write("Замена строки в текстовом файле\nЗаписать список в файл\nИзменить строку в списке\nВставить строку\n")

pos1 = int(input("Введите индекс первой строки: "))
pos2 = int(input("Введите индекс второй строки: "))

f = open("homework22.txt", "r")
rl = f.readlines()
f.close()
# print(rl)

if 0 <= pos1 <= len(rl) and 0 <= pos2 <= len(rl):
    str1 = rl[pos1]
    str2 = rl[pos2]
    rl.pop(pos1)
    rl.insert(pos1, str2)
    rl.pop(pos2)
    rl.insert(pos2, str1)
else:
    print("Вы ввели несуществующий индекс")

print(rl)
f = open("homework22.txt", "w")
f.writelines(rl)
f.close()
