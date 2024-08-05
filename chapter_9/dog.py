class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Init name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in respond to command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a commoand"""
        print(f"{self.name} rolled over!")

my_dog = Dog("rio",30)
my_dog.roll_over()
my_dog.sit()
my_dog.name
my_dog.age
