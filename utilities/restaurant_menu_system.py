class Menu():

    currency = "₱"

    def __init__(self):
        self.menu_items = []

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def remove_item(self, menu_item):
        self.menu_items.remove(menu_item)

    def show_menu(self):
        for item in self.menu_items:
            print(item)

    @property
    def total_items(self):
        return len(self.menu_items)

    def __str__(self):
        return f"The menu currently has {self.total_items} items."

class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {Menu.currency}{self.price}"

class Drink(MenuItem):

    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.temperature = temperature

    def __str__(self):
        return super().__str__() + f" ({self.temperature})"

class Food(MenuItem):

    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor

    def __str__(self):
        return super().__str__() + f" ({self.flavor})"

class Dessert(Food):

    def __init__(self, name, price, flavor, sweetness_level):
        super().__init__(name, price, flavor)
        self.sweetness_level = sweetness_level

    def __str__(self):
        return super().__str__() + f", Sweetness Level: {self.sweetness_level}/10"

class Juice(Drink):

    def __init__(self, name, price, temperature, flavor):
        super().__init__(name, price, temperature)
        self.flavor = flavor

    def __str__(self):
        return super().__str__() + f", {self.flavor}"

menu1 = Menu()

pork_hamlet = MenuItem("Pork Hamlets", 150)
chocolate = Drink("Chocolate", 169, "Cold")
sinigang = Food("Sinigang", 120, "Sour")
leche_flan = Dessert("Leche Flan", 75, "Sweet", 5)
orange_juice = Juice("Orange", 15, "Cold", "Sweet")

menu1.add_item(pork_hamlet)
menu1.add_item(chocolate)
menu1.add_item(sinigang)
menu1.add_item(leche_flan)
menu1.add_item(orange_juice)

print(pork_hamlet)
print(chocolate)
print(sinigang)
print(leche_flan)
print(orange_juice)

menu1.remove_item(leche_flan)

menu1.show_menu()
print(menu1.total_items)
print(menu1)
