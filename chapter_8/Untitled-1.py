def get_formatted_name(first_name, last_name, middle_name =''):
    full_name = ""
    if middle_name:
        full_name  = (f"{first_name} {middle_name} {last_name}")
    else:
        full_name = (f"{first_name} {last_name}")
    return full_name.title()


print(get_formatted_name("aly","aboud"))
print(get_formatted_name("aly", "aboud", "abdelshafy"))


def build_person(first_name, last_name):
    person = {'first':first_name,'last' :last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person_1(first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person

print(build_person_1('aly','aboud', 30))

def enter_your_age():
    age_input = input("Please enter your age (optional): ")
    age = 0
    if age_input:
        try:
            age = int(age_input)
            print(f"this is age {age}")
        except:
            print("you entered a wrong format age")
            enter_your_age()
    return age

print("tell us more about you")
f_name = input("First name: ")
l_name = input("Last namea: ")
age = enter_your_age()
print(age)
print(build_person_1(first_name=f_name, last_name= l_name, age = age))



def enter_string(message): 
    user_input = input(message)
    return user_input


def city_country(city_name, country_name):
    print(f"{city_name}, {country_name}")

for i in range(3):
    print("enter 'q' at any time to quit")
    city_name = enter_string("Please enter city name: ")
    if(city_name == 'q'):
        break
    country_name = enter_string("Please enter country name: ")
    if (country_name == 'q'):
        break
    city_country(city_name= city_name, country_name= country_name)

        

