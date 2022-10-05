class Pizza:
    def __init__(self, diameter, toppings, crust, price, slices=8):
        self.diameter = diameter
        self.toppings = toppings #list of Topping objects
        self.crust = crust
        self.price = price
        self.slices = slices

    def eat_slices(self, number):
        self.slices -= number

    def print_toppings(self):
        for topping in self.toppings:
            print(topping.name)

    def get_total_topping_cals(self):
        topping_cals = 0
        for topping in self.toppings:
            topping_cals += topping.get_total_cals()
        return topping_cals
    
    def add_topping_considering_preference(self, veg_preference, new_topping_to_add):
    #veg_preference is True if prefer only vegetarian toppings. Not an attribute of pizza, but
    # a new argument for a user to pass in.
        if veg_preference and new_topping_to_add.vegetarian:
            self.toppings.append(new_topping_to_add)
        else:
            raise Exception("Tried to add a non-vegetarian topping to vegetarian preference.")

    def print_description(self):
        print(f"My pizza costs ${self.price} dollars and has {self.slices} slices")
