import random

tpl1 = tuple(random.randint(0, 5) for _ in range(10))
tpl2 = tuple(random.randint(-5, 0) for _ in range(10))
print(tpl1)
print(tpl2)
concat = tpl1 + tpl2
print(concat)
count_0 = concat.count(0)
print(f"Количество 0 в третьем кортеже: {count_0}")
