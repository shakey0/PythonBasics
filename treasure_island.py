import random


def get_choice(choices, correct):
  message = "\nPress "
  for item in choices:
    message += item + " " + choices[item][0] + " or "
  message = message[:-4] + "."
  choice = input(message + "\n").upper()
  while True:
    if choice == correct:
      print(choices[correct][1])
      break
    elif choice not in choices.keys():
      print("\nUnrecognised choice!")
      choice = input().upper()
    else:
      print("\n" + choices[choice][1])
      print("\nGAME OVER!")
      exit()


# Welcome and first part of the game (which is set)
print("Welcome to Treasure Island!")
input("Press Enter to begin.")
get_choice({"R": ["to go RIGHT", "You fell into a hole!"],
            "L": ["to go LEFT", "Phew! You avoided a very big hole!"]},
          "L")

# Next part of the game where the player has to choose the correct amount of time to wait (random)
messages = {"S": ["You were swallowed by a whale!", "You picked the right moment!"], "W": ["You were eaten by a giant roc!", "Patience is a virtue."]}
waiting = random.randint(1, 2)
next_part = "W"
swim_message, wait_message = messages["S"][0], messages["W"][1]
for number in range(waiting+1):
  if number == waiting:
    next_part = "S"
    swim_message, wait_message = messages["S"][1], messages["W"][0]
  get_choice({"S": ["to SWIM", swim_message],
              "W": ["to WAIT", wait_message]},
            next_part)
  
# Last part of the game where the player has to choose between 4 doors (random)
print("\nYou have come to a cave with 4 mysterious doors.")
doors = {"Y": "yellow", "B": "blue", "R": "red", "G": "green"}
correct_door = random.choice(list(doors.keys()))
doors_messages = {}
for door in doors:
  if door == correct_door:
    doors_messages[door] = [f"to open the {doors[door]} door", f"You picked the right door! You opened the {doors[door]} door and found the treasure!"]
  else:
    doors_messages[door] = [f"to open the {doors[door]} door", f"Bad luck! You opened the {doors[door]} door and were eaten by a huge monster!"]
get_choice(doors_messages, correct_door)
print("You did it! Well done!")