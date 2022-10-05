from food.pizza import Pizza
from food.frozen_pizza import FrozenPizza
from pizzacomponents.topping import Topping

pineapple_topping = Topping("pineapple",True,50,False,"extra")
bacon_topping = Topping("bacon", False, 80, False, "regular")
mushroom_topping = Topping("mushroom", True, 70, False, "extra")

hawaiian_pizza = Pizza(21, [pineapple_topping, bacon_topping], "thin", 9.99, 8)
frozen_veggie = FrozenPizza(10, [mushroom_topping], "stuffed", 5.99, 8)

def add_tomato_and_eat(my_pizza):
    my_pizza.toppings.append("tomato")
    print(my_pizza.toppings)
    my_pizza.eat_slices(1)
    print(my_pizza.slices)
    

    
#commented out to demonstrate lines of code below.
#add_tomato_and_eat(hawaiian_pizza)
#add_tomato_and_eat(frozen_veggie)
hawaiian_pizza.print_toppings()
print(hawaiian_pizza.get_total_topping_cals())

#trying to add a non-vegetarian pizza - an exception is raised
my_veg_preference = True
frozen_veggie.add_topping_considering_preference(my_veg_preference, bacon_topping)