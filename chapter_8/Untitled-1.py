
def describe_pet(animal_type, pet_name ='harry'):
    print(f"i have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet("dog")
describe_pet(animal_type="bird", pet_name="lara")

#Exercise 8.3
def make_shirt(message, size = "large" ):
    print(f"The size of the shirt is {size} and message is {message}")

make_shirt("Hello to my world","xl")
make_shirt(message="Python rocks")


def get_formatted_name(first_name, last_name):
    """Return full name , neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name

full_name = get_formatted_name("aly","aboud")
print(full_name.title())