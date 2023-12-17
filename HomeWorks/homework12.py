# Дан словарь. Создать новый словарь, который будет содержать только имя и зарплату сотрудника, а затем удалить
# эти значения из исходного словаря

dict_first = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
for key in dict_first:
    if key == "name":
        name_key = key
        name_value = dict_first[key]
    if key == "salary":
        salary_key = key
        salary_value = dict_first[key]
dict_first.pop("name")
dict_first.pop("salary")
print(dict_first)
dict_res = {name_key: name_value, salary_key: salary_value}
print(dict_res)
