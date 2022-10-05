from .pizza import Pizza

class FrozenPizza(Pizza):
    def __init__(self, diameter, toppings, crust, price, slices=8):
        super().__init__(diameter, toppings, crust, price, slices)
        self.defrosted = False

    def defrost(self):
        self.defrosted = True

    def eat_slices(self, number):
        if not self.defrosted:
            raise Exception("Don't break your teeth")
        super().eat_slices(number)