# Посчитать количество гласных букв в строке

s = input("Введите строку: ")
count = 0
letter = {"а", "е", "ё", "и", "о", "у", "э", "ю", "я", "ы", "А", "Е", "Ё", "И", "О", "У", "Э", "Ю", "Я", "Ы"}
for i in letter:
    for j in s:
        if i == j:
            count += 1
print(f"Количество гласных букв равно: {count}")
