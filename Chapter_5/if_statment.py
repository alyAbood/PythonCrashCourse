cars = ['audi', 'bmw', 'subaru', 'toyta','hyndai']
for car in cars:
    if(car != 'bmw'):
        print(car.upper())
    else:
        print(car.title())   


car_aly = 'tuscan'
if(car_aly not in  cars):
    print("Aly car is not in the list")



car  = 'subaru'

age  = 30
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


fee = 0

if age <4:
    print("You are free to enter")
elif age <=18:
    fee = 25
else:
    fee = 40


if(fee > 0):
    print (f"your admission will be {fee}")
else:
    print("Your admission will be free")


car = 'hyndai'

if car not in cars:
    print("Hyndai is not in the car list")
else:
    print("Hyndai is in the list")

my_car = 'subaru'

print("Is car == 'subaru'? I predict true")
print(my_car == 'subaru')



