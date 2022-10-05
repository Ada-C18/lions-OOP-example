import pytest
from food.pizza import Pizza
#from path to module (package.module) import classes, functions, variables, or everything (*)

def test_pizza_creation():
    #arrange, #act
    hawaiian_pizza = Pizza(21,"thin", 9.99, 8, ["pineapple", "bacon"])

    #assert
    assert(hawaiian_pizza.diameter == 21)
    assert(hawaiian_pizza.toppings == ["pineapple", "bacon"])
    assert(hawaiian_pizza.crust == "thin")
    assert(hawaiian_pizza.price == 9.99)
    assert(hawaiian_pizza.slices == 8)

@pytest.mark.skip() #optional/default parameters not implemented - skip
def test_no_toppings_given_converts_to_empty_list():
    #arrange, act
    empty_pizza = Pizza()

    #assert
    assert(empty_pizza.toppings == [])


def test_eat_slices_decreases_num_slices():
    #arrange
    hawaiian_pizza = Pizza(21,"thin", 9.99, 8, ["pineapple", "bacon"])

    #act
    hawaiian_pizza.eat_slices(4)

    #assert
    assert(hawaiian_pizza.slices == 4)

def test_add_topping_adds_a_new_topping():
    #arrange
    hawaiian_pizza = Pizza(21,"thin", 9.99, 8, ["pineapple", "bacon"])

    #act
    hawaiian_pizza.add_topping("canadian bacon")

    #assert
    assert(len(hawaiian_pizza.toppings)==3)
    assert(hawaiian_pizza.toppings[2] == "canadian bacon")

@pytest.mark.skip() #optional/default parameters not implemented - skip
def test_given_pizza_toppings_is_empty_evals_to_empty_list():
    #arrange, act
    hawaiian_pizza = Pizza(diameter=21, crust="thin", price=9.99, slices=8)

    #assert
    assert(hawaiian_pizza.toppings == [])
