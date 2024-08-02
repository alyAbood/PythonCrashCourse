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