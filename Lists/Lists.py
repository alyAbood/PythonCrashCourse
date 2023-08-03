# create list
bicycles = ["trek", "cannodndale", "redline", "speciaized"]
print(bicycles)

#print element
print(bicycles[0])

#use string methods in array
#title method make string starts with caps
print(bicycles[0].title())

#return last element in the list
print(bicycles[-1])

#When use negative index it means you want that inded from the end
print(bicycles[-2].title())

#Applying string concation with array items

message = "My first bicycle was a "+ bicycles[0].title()+ "."
print(message)




