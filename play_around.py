def as_sun_lover(temperature):
    if temperature >= 25:
        return "great"
    else:
        return "not great"
    
def as_snow_lover(temperature):
    if temperature <= 0:
        return "great"
    else:
        return "not great"
    
def report_weather(temperature, preferred_weather):
    message = preferred_weather(temperature)
    return message

print(report_weather(0, as_snow_lover))


passwords = [
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]
print(next(filter(lambda password: password['service'] == 'acebook', passwords)))

list_of_felines = ["lion", "tiger", "leopard", "jaguar", "snow leopard", "clouded leopard", "lynx",
                   "puma", "cheetah", "wildcat"]

has_leopard_in_name = list(filter(lambda feline: "leopard" in feline, list_of_felines))
has_leopard = [feline for feline in list_of_felines if "leopard" in feline]

felines_starting_with_l = list(filter(lambda feline: feline[0] == "l", list_of_felines))
starts_with_l = [feline for feline in list_of_felines if feline[0] == "l"]

print(has_leopard_in_name)
print(has_leopard)
print(felines_starting_with_l)
print(starts_with_l)

dictionary = {"Colour": "Red", "Size": "Large", "Type": "Pretty"}

for i in dictionary.items():
    print(i)

for item in dictionary:
    print(f"Key is {item}, and Value is {dictionary[item]}")

import random

animals = ["Zebra", "Monkey", "Rhino", "Hippo"]
people = ["John", "Kate", "Debbie", "Sally", "Ben", "Lizzy"]

assign_animal = {person: random.choice(animals) for person in people}
print(assign_animal)

special_cases = {"Merry": "Fox", "John": "Tiger", "Sally": "Lion"}
assign_animal.update(special_cases)
print(assign_animal)

new_dict = {person: random.choice(animals) for person in people}

print(new_dict)

new_strings = ["cat", "dog", "rabbit", "fox", "ostrich", "hippopotamus"]
add_es1, add_es2 = ["s", "x"], ["sh", "ch"]

# NOTE: using if else statements with lambda
print(list(map(lambda word: word + "s" if word[-1] not in add_es1 and word[-2:] not in add_es2 else word + "es",
               new_strings)))

# NOTE: using if else statements with list comprehension
print([word + "s" if word[-1] not in add_es1 and word[-2:] not in add_es2 else word + "es" for word in new_strings])

# NOTE: filtering a list with lambda based on a condition (not used to make changes to the words)
print(list(filter(lambda word: word[-1] not in add_es1 and word[-2:] not in add_es2, new_strings)))

print(dict(zip([num+1 for num in range(6)], new_strings)))

print(dict(cat=9, dog=5, bird=2))

list1 = ["blue", "red", "yellow"]
list2 = ["car", "bus", "train"]

combined = {colour: thing for (colour, thing) in zip(list1, list2)}
print(combined)

num_list = [1, 2, 3, 4, 5, 6]

cards = ["cat", "dog", "hamster", "parrot", "rabbit", "snake"]

random.shuffle(num_list)

draw_pile = {num:card for (num, card) in zip(num_list, cards)}

print(draw_pile)
print(list(draw_pile.values()))

letter = "r"
chosen_num = next(filter(lambda item: item[1][0] == letter, draw_pile.items()))[0]
print(chosen_num)

print(draw_pile.get(2))

print(list(map(lambda item: item+3, num_list)))

wins = {"r": [1, "s"], "p": [2, "r"], "s": [3, "p"]}
choices = list(wins.keys())
print(choices)
user_choice = ""
computer_choice = random.choice(choices)
print(computer_choice)

a_string = "Hello World"

a_string.replace()
print(a_string)
