import random
from list_of_animals import animal_list
from list_of_first_names import first_name_list

class Guest():

    def __init__(self):
        self.all_guests = {}

    def create_guest(self):
        age_bracket = random.randint(1, 20)
        if age_bracket == 1:
            age = random.randint(4, 6)
            weight = random.randint(15, 25)
            height = random.randint(90, 120)
        elif age_bracket <= 4:
            age = random.randint(7, 11)
            weight = random.randint(20, 50)
            height = random.randint(120, 150)
        elif age_bracket <= 11:
            age = random.randint(12, 17)
            weight = random.randint(35, 75)
            height = random.randint(140, 190)
        elif age_bracket <= 15:
            age = random.randint(18, 23)
            weight = random.randint(45, 90)
            height = random.randint(150, 190)
        elif age_bracket <= 19:
            age = random.randint(24, 45)
            weight = random.randint(45, 100)
            height = random.randint(150, 190)
        else:
            age = random.randint(46, 75)
            weight = random.randint(50, 100)
            height = random.randint(150, 190)
        very_heavy = random.randint(1, 5)
        if age > 22 and very_heavy == 5:
            weight += 30
        very_tall = random.randint(1, 5)
        if age > 17 and very_tall == 5:
            height += 20
        favourite_animal = animal_list()
        guest_name = first_name_list()
        while True:
            unique_number = random.randint(1, 999999)
            if unique_number not in self.all_guests.keys():
                break
        self.all_guests[unique_number] = {"name":guest_name, "age":age, "weight(kg)":weight, "height(cm)":height,
                                          "favourite animal":favourite_animal}

    def print_all_guest_data(self):
        formatted_message = ""
        for guest in self.all_guests:
            for item in self.all_guests[guest]:
                formatted_message += item.title() + ": " + str(self.all_guests[guest][item]) + "   "
            formatted_message += "\n"
        print(formatted_message)

    def print_guest_data(self, ordered):
        formatted_message = ""
        for guest in ordered:
            for place in guest:
                if not isinstance(place, int):
                    for item in place:
                        formatted_message += item.title() + ": " + str(place[item]) + "   "
            formatted_message += "\n"
        print(formatted_message)

    def print_arranged_guest_data(self, order):
        ordered = sorted(self.all_guests.items(), key=lambda x: x[1][order])
        self.print_guest_data(ordered)

guests = Guest()
for number in range(100):
    guests.create_guest()

guests.print_arranged_guest_data("favourite animal")
