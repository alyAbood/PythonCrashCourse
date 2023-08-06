
motorcycles = ['honda', 'yamaha', 'suziki']
#print(motorcycles)

motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('honda')
#print(motorcycles)


#Remove element from list
del motorcycles[0]
#print(motorcycles)

#remove element from list
del motorcycles[1]
#print(motorcycles)

# pop last element
motorcycles = ['honda', 'yamaha', 'suziki']
popped_moto = motorcycles.pop()
#print(motorcycles)
#print(popped_moto)

#pop element at position
motorcycles = ['honda', 'yamaha', 'suziki']
popped_moto = motorcycles.pop(1)
#print(popped_moto)

#use del when you want to remove item and you don't need the value
#use pop when you want to remove item and you want work on item



#Remove item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive.title() + " is too expensive")













