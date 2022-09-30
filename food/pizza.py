class Pizza:
    def __init__(self, diameter=None, crust=None, price=None, slices=None, toppings=None):
        #demonstration of setting default parameters (None)
        #you can have a mix of required parameters and optional ones. Set optional ones at the end of the constructor.
        #setting mutable values as default parameters is not recommended.
        self.diameter = diameter
        self.crust = crust
        self.price = price
        self.slices = slices
        if not toppings:
            self.toppings = []
            #warning to not set mutable values in the constructor to avoid potential problems with side effects
        else:
            self.toppings = toppings

    def eat_slices(self, number):
        self.slices -= number

    def add_topping(self, new_topping):
        self.toppings.append(new_topping)

    def print_description(self):
        print(f"My pizza costs ${self.price} dollars and has {self.slices} slices")
        #not easily testable because it is not returning or modifying anything, just accessing.


hawaiian_pizza = Pizza(21, "thin", 9.99, 8, ["pineapple", "bacon"])
veggie_pizza = Pizza(10, "stuffed", 5.99, 8, ["mushroom", "olives"])

hawaiian_pizza.toppings[0] = 'peach'
print(hawaiian_pizza.toppings)

veggie_pizza.random = 4
print(veggie_pizza.random)
#demo that you can set a new variable parameter outside of the class definition. (not recommended as it can make the program unpredictable. developers often rely on having all parameters documented in the constructor, whether they are optional or not.)

veggie_pizza.eat_slices(4)
hawaiian_pizza.print_description()
veggie_pizza.print_description()
