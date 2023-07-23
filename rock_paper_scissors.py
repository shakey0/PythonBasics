rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

print("\nWelcome to ~ROCK~PAPER~SCISSORS~!")
print("\nHow many rounds would you like to play?\nEnter an ODD number between 0 and 32.")
num_rounds = ""
while True:
  num_rounds = input("")
  if num_rounds.isnumeric() and 0 < int(num_rounds) < 32:
    if int(num_rounds) % 2 == 0:
      print("\nMust be an odd number!")
    else:
      break
  else:
    if not num_rounds.isnumeric():
      print("\nIs that a number?")
    else:
      print("\nInvalid command!")
num_rounds = int(num_rounds)
wins = {"r": [rock, "s"], "p": [paper, "r"], "s": [scissors, "p"]}
choices = list(wins.keys())
player_score, computer_score = 0, 0
print("\nThe game has begun!")
count = 1
while count <= num_rounds:
  if player_score > num_rounds // 2 or computer_score > num_rounds // 2:
    print("\nIt's early, but a clear winner has been found!")
    input("\nPress Enter to continue.")
    break
  print(f"\n\nROUND: {count} of {num_rounds}")
  print(f"\nYour score: {player_score}")
  print(f"Computer score: {computer_score}")
  while True:
    user_choice = ""
    computer_choice = random.choice(choices)
    print("\nPress R for ROCK, P for PAPER, or S for SCISSORS.")
    while True:
      user_choice = input("")
      if user_choice.lower() in choices:
        break
      else:
        print("\nUnrecognised choice!")
    print("\nYOU:\n" + wins[user_choice][0])
    print("\nCOMPUTER:\n" + wins[computer_choice][0])
    if user_choice == computer_choice:
      print("\nThat's the same! Again!")
    else:
      break
  winner = False
  for item in wins:
    if item == user_choice and wins[item][1] == computer_choice:
      winner = True
  if winner:
    print("\nThat's 1 up for you!")
    player_score += 1
  else:
    print("\nAwww, how unlucky.")
    computer_score += 1
  input("\nPress Enter to continue.")
  count += 1
print(f"\nYour final score: {player_score}")
print(f"Computer's final score: {computer_score}")
if player_score > computer_score:
  print(f"\nYou won by {player_score - computer_score}!")
else:
  print(f"\nUnlucky! The computer beat you by {computer_score - player_score}.")
