class Pizza:
    def __init__(self, diameter=None, crust=None, price=None, slices=None, toppings = []):
        self.diameter = diameter
        self.toppings = toppings
        self.crust = crust
        self.price = price
        self.slices = slices
        
    def eat_slices(self, number):
        self.slices -= number

    def add_topping(self, new_topping):
        self.toppings.append(new_topping)

    def print_description(self):
        print(f"My pizza costs ${self.price} dollars and has {self.slices} slices")


hawaiian_pizza = Pizza(21, "thin", 9.99, 8, ["pineapple", "bacon"])
veggie_pizza = Pizza(10, "stuffed", 5.99, 8, ["mushroom", "olives"])
print(hawaiian_pizza.toppings)
hawaiian_pizza.toppings[0] = 'peach'
print(hawaiian_pizza.toppings)

veggie_pizza.random = 4

veggie_pizza.eat_slices(4)
hawaiian_pizza.print_description()
veggie_pizza.print_description()