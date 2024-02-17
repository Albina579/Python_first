class Car:
    def __init__(self, model, year, produce, power, color, price):
        self.model = model
        self.year = year
        self.produce = produce
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.produce}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_produce(self):
        return self.produce

    def get_power(self):
        return self.power

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


car1 = Car("X7 M50i", 2021, "BMV", "500 л.с.", "white", 10790000)
car1.print_info()
print(car1.get_model())
print(car1.get_color())
