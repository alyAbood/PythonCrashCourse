class Car:
    def __init__(self, make, model, year):
        """init attributes that describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a good formatted name"""
        long_name = (f"{self.make} {self.model} {self.year}")
        return long_name.title()
    
    def read_odometer(self):
        """print a statment showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def check_milage(self, milage):
        if(milage < self.odometer_reading):
            print("You can't roll back an odometer!")
            return False
        else:
            return True
    
    def set_mileage(self, mileage):
        """Set the odometer reading to a given value"""
        if(self.check_milage(mileage)):
            self.odometer_reading = mileage
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Show the car has a gas tank"""
        print("This car has a gase tank!")
       
my_new_car = Car("hyndai", "i10", "2012")
print(my_new_car.get_descriptive_name())
my_new_car.set_mileage(30)
my_new_car.set_mileage(15)
my_new_car.read_odometer()

class Battery:
    def __init__(self, battery_size = 40):
        self.batter_size = battery_size
    
    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.batter_size}-KWH battery.")
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vechiles"""
    def __init__(self, make, model, year):
        """Init attributes of the parent class"""
        super().__init__(make,model,year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("Electric cars has no fuel tank")
    


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
