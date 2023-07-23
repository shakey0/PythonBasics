first_list = [1, 2, 3, 4, 5]
second_list = ["one", "two", "three", "four", "five"]

combined = {first:second for (first, second) in zip(first_list, second_list)}

print(combined)

dict_one = {"Y": "yellow", "B": "blue", "R": "red", "G": "green"}
dict_two = {"car": "yellow", "bike": "blue", "canoe": "red", "boat": "green"}

things_messages = {colour:thing for (colour, thing) in zip(dict_two.keys(), dict_one.keys())}
print(things_messages)