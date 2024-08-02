def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza("mushroom", "green peppers", "extra cheese")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
user_profile = build_profile("aly","aboud",location = "alexandria", field = "physics")
print(user_profile)


def extras_on_sandwishes(*toppings):
    for topping in toppings:
        print(f"i have added {topping}")
    print("i finished all topping on my sandwish\n")

extras_on_sandwishes("pasta","chicken", "white sauce")
extras_on_sandwishes("meat","red sauce","vegetables")
extras_on_sandwishes("meat", "soap", "chicken", "fries")


def build_car(manufacturer, model_name, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model_name"] = model_name
    return car_info

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
