class Person:
    def __init__(self, name, age):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Имя введено не корректно")
        if isinstance(age, int):
            self.__age = age
        else:
            print("Возраст введен не корректно")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Имя введено не корректно")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self.__age = new_age
        else:
            print("Возраст введен не корректно")

    @name.deleter
    def name(self):
        del self.__name

    @age.deleter
    def age(self):
        del self.__age


p1 = Person("Irina", 26)
print(p1.__dict__)

p1.name = "Igor"
p1.age = 31
print(f"{p1.name}\n{p1.age}")

del p1.name
print(p1.__dict__)

p2 = Person("Petr", "ten")
print(p2.__dict__)

