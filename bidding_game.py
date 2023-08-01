from list_of_animals import animal_list
import os
import random

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def f_number(number):
    number = str(number)
    if "." not in number:
        return number + ".00"
    else:
        if len(number.rsplit('.')[1]) == 1:
            return number + "0"
        else:
            return number

def get_animal_adjective(animal):
    adjectives_by_letter = {"a":"amaranthine", "b":"benevolent", "c":"cantankerous", "d":"diplomatic",
                            "e":"earnest", "f":"faithful", "g":"godhearted", "h":"high-spirited",
                            "i":"inspiring", "j":"judgemental", "k":"kinky", "l":"lascivious",
                            "m":"magnificent", "n":"nationalistic", "o":"outspoken", "p":"pedantic",
                            "q":"questionable", "r":"rambunctious", "s":"self-absorbed", "t":"tenderhearted",
                            "u":"understanding", "v":"venerable", "w":"warmhearted", "x":"xenodochial",
                            "y":"youthful", "z":"zealous", "ch":"charitable", "cr":"cryptic",
                            "fl":"flirtatious", "fr":"frigid", "gn":"nationalistic", "gr":"greathearted",
                            "sh":"short-sighted", "sn":"snobbish", "sp":"spirited", "sq":"squatting",
                            "st":"stylish", "sw":"Swedish", "tr":"trustful", "ph":"pharaohtypical"}
    if animal[0:2] in adjectives_by_letter.keys():
        return adjectives_by_letter[animal[0:2]]
    else:
        return adjectives_by_letter[animal[0]]

def get_number_of_players():
    while True:
        number = input("\nHow many players are there? ")
        if number.isnumeric() and 1 < int(number) <= 20:
            return int(number)
        else:
            print("\nInvalid command.")

def get_player_name(player_no):
    while True:
        name = input(f"\nPlayer {player_no}, enter your name: ")
        if len(name) > 1 and len([char for char in name if char.isnumeric()]) == 0:
            return name
        else:
            print("\nInvalid name or too short.")

def setup_round():
    animal = animal_list()
    adjective = get_animal_adjective(animal.lower())
    a = "a" if adjective[0] not in "aeiou" else "an"
    print(f"\nYou are bidding to buy {a} {adjective} {animal.lower()}.")
    input("\nPress Enter to continue.")
    return adjective + " " + animal.lower()

def get_player_bid(animal_, name, money, old_player_bid, highest_bid=0):
    os.system('clear')
    print(f"\nCalling: {name.upper()}")
    input("\nPress Enter.")
    if money <= highest_bid or money == 0:
        os.system('clear')
        print(f"\n{name.upper()}! You don't have enough money to compete!")
        input("\nPress Enter for next bidder.")
        return False
    while True:
        os.system('clear')
        print(f"\n{name.upper()}     Remaining money: £{f_number(money)}")
        if highest_bid != 0:
            print(f"\nBid to beat: £{f_number(highest_bid)}     Last bid: £{f_number(old_player_bid)}")
            more = input(f"\nWould you like to raise your bid for the {animal_}?"
                         "\nPress Enter for YES, or N + Enter for NO: ")
            if more == "N" or more == "n":
                return False
        bid = input(f"\nEnter bid amount for the {animal_}: £")
        if not is_float(bid) and not bid.isnumeric():
            input("\nInvalid input.")
            continue
        if money >= float(bid) > highest_bid:
            if '.' not in bid:
                return float(bid)
            elif is_float(bid) and len(bid.rsplit('.')[1]) <= 2:
                return float(bid)
            else:
                input("\nUnrecognised amount of money.")
        elif money < float(bid):
            input("\nYou don't have enough money!")
        elif float(bid) <= highest_bid:
            input("\nBid too low!")

def get_all_bids(player_names, player_money, player_bids, max_bid, animal):
    old_player_bids = player_bids
    player_bids = []
    count = 1
    while count <= len(player_names):
        bid = get_player_bid(animal, player_names[count-1], player_money[count-1], old_player_bids[count-1], max_bid)
        if not bid:
            player_bids.append(old_player_bids[count-1])
        else:
            player_bids.append(bid)
        count += 1
    return player_bids

def get_winner(max_bid_player, player_names, player_points, player_bids, animal):
    os.system('clear')
    print(f"\nA clear winner has been found for this round!"
          f"\nWell done {max_bid_player.upper()}! The {animal} is yours!")
    final_bid_string = "\nFinal bid amounts:\n"
    for name, amount in zip(player_names, player_bids):
        final_bid_string += name + ": £" + str(f_number(amount)) + "\n"
    print(final_bid_string)
    input("Press Enter to continue.")
    player_points[player_names.index(max_bid_player)] += 1
    return player_points

def play_round(player_names, player_money, player_points):
    animal = setup_round()
    player_bids = get_all_bids(player_names, player_money, [0 for _ in player_names], 0, animal)
    max_bid = max(player_bids)
    while True:
        os.system('clear')
        print(f"\nThe highest bid for the {animal} was £{f_number(max_bid)}."
              "\n\nEach player has 1 chance to raise their bid before a winner is delared.")
        input("\nPress Enter to continue.")
        player_bids = get_all_bids(player_names, player_money, player_bids, max_bid, animal)
        max_bid = max(player_bids)
        if player_bids.count(max_bid) > 1:
            os.system('clear')
            print(f"\nThe highest bid is tied at {f_number(max_bid)}!")
            input("Press Enter to continue.")
            continue
        else:
            break
    max_bid_player = player_names[player_bids.index(max_bid)]
    player_points = get_winner(max_bid_player, player_names, player_points, player_bids, animal)
    return [round(money - bid, 2) for money, bid in zip(player_money, player_bids)], player_points

def show_all_money(player_names, player_money):
    money_left = "\nAmount of money remaining:\n"
    for name, amount in zip(player_names, player_money):
        money_left += name + ": £" + str(f_number(amount)) + "\n"
    os.system('clear')
    print(money_left)
    input("Press Enter to continue.")

def show_all_points(player_names, player_points):
    total_points = "\nPlayer Scores:\n"
    for name, points in zip(player_names, player_points):
        total_points += name + ": " + str(points) + "\n"
    os.system('clear')
    print(total_points)
    input("Press Enter to continue.")

def get_final_winner(player_names, player_points):
    max_points = max(player_points)
    if player_points.count(max_points) > 1:
        all_winners = [player for player, points in zip(player_names, player_points) if points == max_points]
        all_winners_message = [name + f" won with {max_points}" for name in all_winners]
        return "\nIt was a draw! The winners are: \n" + "\n".join(all_winners_message)
    else:
        return f"\n{player_names[player_points.index(max_points)]} won with {max_points} points!"

def play_game():
    print("\nWelcome to the animal bidding game!")
    number_of_players = get_number_of_players()
    number_of_rounds = number_of_players + 1
    player_names = []
    for number in range(number_of_players):
        player_name = get_player_name(number+1)
        player_names.append(player_name)
    money = random.randint(2, 50)
    player_money, player_points = [money for _ in player_names], [0 for _ in player_names]
    for round in range(number_of_rounds):
        show_all_money(player_names, player_money)
        os.system('clear')
        print(f"\nRound {round+1} of {number_of_rounds}")
        player_money, player_points = play_round(player_names, player_money, player_points)
        show_all_points(player_names, player_points)
        if all(money == 0 for money in player_money):
            os.system('clear')
            print("\nYou've all used up your money!")
            input("\nPress Enter to continue.")
            break
    os.system('clear')
    print(get_final_winner(player_names, player_points))

play_game()