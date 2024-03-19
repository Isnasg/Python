class Home:
    def check (self, city, street, home, flat):
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat

    def info(self):
        print(f"City: {self.city}")
        print(f"Street: {self.street}")
        print(f"Home: {self.home}")
        print(f"Flat: {self.flat}")

    def prank(self):
        print("Тебя вычислили!")
# Пример использования
home1 = Home("Екатеринбург", "Бардина", 48, 12)
home2 = Home("Челябинск", "Ленина", 28, 139)

home1.display_info()
home1.prank()

home2.display_info()
home2.prank()