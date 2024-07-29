def greet_user():
    """displaying a simple greeting"""
    print("Hello")

greet_user()


def greet_user_by_name(username):
    """Display a simple greeting with name"""
    print(f"Hello, {username.title()}")


greet_user_by_name("aly")


#Exercise 8.1

def display_message():
    print("I am learning chpater 8 about functions")

display_message()

#Exercise 8.2

def favorite_book(title):
    print(f"One of my favourite books is {title.capitalize()}")


favorite_book("alice in wonderland")