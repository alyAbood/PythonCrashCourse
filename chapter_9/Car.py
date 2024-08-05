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
    
    def update_mileage(self, mileage):
        """Set the odometer reading to a given value"""
        if(self.check_milage(mileage)):
            self.odometer_reading = mileage
        else:
            return


my_new_car = Car("hyndai", "i10", "2012")
print(my_new_car.get_descriptive_name())
my_new_car.update_mileage(30)
my_new_car.update_mileage(15)
my_new_car.read_odometer()
