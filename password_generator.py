#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def is_valid_num(num, type_):
    if not num.isnumeric():
        print("\nUnrecognised choice!")
        return False
    elif int(num) <= 0:
        print(f"\nPassword must include at least 1 {type_}!")
        return False
    return True


def get_from_user(type_):
    while True:
        num_of = input(f"\nHow many {type_}s would you like in your password?\n")
        if is_valid_num(num_of, type_):
            return num_of


def get_char_quantities():
    while True:
        num_of_letters = get_from_user("letter")
        num_of_numbers = get_from_user("number")
        num_of_symbols = get_from_user("symbol")
        total = int(num_of_letters) + int(num_of_numbers) + int(num_of_symbols)
        if 6 <= total <= 30:
            break
        else:
            print("\nPassword must be between 6 and 30 characters inclusive.")
    return int(num_of_letters), int(num_of_numbers), int(num_of_symbols)


def pick_random(number_of, from_list):
    return [random.choice(from_list) for _ in range(number_of)]


def random_shuffle(chars_in_password):
    random.shuffle(chars_in_password)
    count = 0
    while count < len(chars_in_password):
        if chars_in_password[count] == chars_in_password[count - 1]:
            random.shuffle(chars_in_password)
            count = 0
        count += 1
    return "".join(chars_in_password)


print("\nWelcome to the PyPassword Generator!")
nr_letters, nr_numbers, nr_symbols = get_char_quantities()
chars_in_password = []
chars_in_password += pick_random(nr_letters, letters)
chars_in_password += pick_random(nr_numbers, numbers)
chars_in_password += pick_random(nr_symbols, symbols)
password = random_shuffle(chars_in_password)
print(f"\n\nYour password is:  {password}")
