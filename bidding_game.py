from list_of_animals import animal_list
import os

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

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


def get_player_name(player_no):
    while True:
        name = input(f"\nPlayer {player_no}, enter your name: ")
        if len(name) > 1 and len([char for char in name if char.isnumeric()]) == 0:
            return name
        else:
            print("\nInvalid name or too short.")

def get_player_bid(animal_, highest_bid=0, name=""):
    while True:
        if name != "":
            more = input(f"\nCalling: {name.upper()}"
                         f"\nWould you like to raise your bid for the {animal_}?"
                         "\nPress Enter for YES, or any key + Enter for NO. ")
            if more != "":
                return False
        bid = input(f"\nEnter bid amount for the {animal_}: £")
        if (is_float(bid) or bid.isnumeric()) and float(bid) > highest_bid:
            if '.' not in bid and bid.isnumeric():
                return float(bid)
            elif is_float(bid) and len(bid.rsplit('.')[1]) <= 2:
                return float(bid)
            else:
                print("\nInvalid input.")
        elif (is_float(bid) or bid.isnumeric()) and float(bid) <= highest_bid:
            print("\nBid too low!")
        else:
            print("\nInvalid input.")

def get_number_of_players():
    while True:
        number = input("\nHow many players are there? ")
        if number.isnumeric() and 1 < int(number) <= 20:
            return int(number)
        else:
            print("\nInvalid command.")

def setup_round():
    print("\nWelcome to the animal bidding game!")
    number_of_players =  get_number_of_players()
    animal = animal_list()
    adjective = get_animal_adjective(animal.lower())
    print(f"\nYou are bidding to buy a {adjective} {animal.lower()}.")
    input("\nPress Enter to continue.")
    return number_of_players, animal, adjective

def first_round(number_of_players, animal, adjective):
    player_names, player_bids = [], []
    count = 1
    while count <= number_of_players:
        os.system('clear')
        name = get_player_name(count)
        player_names.append(name)
        bid = get_player_bid(adjective + " " + animal.lower())
        player_bids.append(bid)
        count += 1
    return player_names, player_bids

def subsequent_rounds(player_names, player_bids, max_bid, animal, adjective):
    old_player_bids = player_bids
    player_bids = []
    count = 1
    while count <= len(player_names):
        os.system('clear')
        print(f"\nBid to beat: £{max_bid}")
        bid = get_player_bid(adjective + " " + animal.lower(), max_bid, player_names[count-1])
        if not bid:
            player_bids.append(old_player_bids[count-1])
        else:
            player_bids.append(bid)
        count += 1
    return player_bids

def play_game():
    number_of_players, animal, adjective = setup_round()
    player_names, player_bids = first_round(number_of_players, animal, adjective)
    max_bid = max(player_bids)
    max_bid_player = player_names[player_bids.index(max_bid)]
    while True:
        os.system('clear')
        print(f"\nThe highest bid for the {adjective} {animal.lower()} was £{max_bid}."
              "\nEach player has 1 chance to raise their bid before a winner is delared.")
        input("Press Enter to continue.")
        player_bids = subsequent_rounds(player_names, player_bids, max_bid, animal, adjective)
        max_bid = max(player_bids)
        max_bid_player = player_names[player_bids.index(max_bid)]
        if player_bids.count(max_bid) > 1:
            os.system('clear')
            print("\nThe highest bid is tied!")
            input("Press Enter to continue.")
            continue
        else:
            break
    max_bid_player = player_names[player_bids.index(max_bid)]
    print(f"\nA clear winner has been found!"
          f"\nWell done {max_bid_player.upper()}! The {adjective} {animal.lower()} is yours!")
    final_bid_string = "\nFinal bid amounts:\n"
    for name, amount in zip(player_names, player_bids):
        final_bid_string += name + ": £" + str(amount) + "\n"
    print(final_bid_string)
    
play_game()