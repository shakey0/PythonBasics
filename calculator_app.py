

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_number(ordinal, saved_letters):
    while True:
        number = input(f"\n{ordinal} number: ")
        if number == "R" or number == "r":
            return "r"
        elif number in saved_letters.keys():
            return saved_letters[number]
        elif number.isnumeric():
            return int(number)
        elif is_float(number):
            return float(number)
        else:
            print("\nInvalid input.")

def get_operator():
    operator = ""
    operators = ["+", "-", "*", "/"]
    while operator not in operators:
        operator = input("\nWhat would you like to do to this number?"
                         "\nType the symbol and press Enter: ")
        if operator == "R" or operator == "r":
            return "r"
        elif operator in operators:
            return operator
        else:
            print("\nUnrecognised command!")

def process_calculation(num1, opp, num2):
    if opp == "+":
        return round(num1 + num2, 8)
    elif opp == "-":
        return round(num1 - num2, 8)
    elif opp == "*":
        return round(num1 * num2, 8)
    else:
        return round(num1 / num2, 8)

def get_y_or_n_choice(asking):
    while True:
        print(f"\n{asking}?"
              "\nPress Y + Enter for YES, or N + Enter for No: ")
        while True:
            choice = input("")
            choice = choice.lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("\nWhat does that mean?"
                      "\nPress Y + Enter for YES, or N + Enter for No: ")

def get_save_letter():
    print("\nEnter a letter or letter combination for your saved number: ")
    while True:
        save_letter = input("")
        if save_letter == "R" or save_letter == "r":
            print("\nThe letter R is reserved. Choose another letter.")
        if save_letter.isalpha() and len(save_letter) <= 3:
            return save_letter
        elif len(save_letter) > 3:
            print("\nToo long!")
        else:
            print("\nMust consist of only letters from the alphabet!")

def use_calculator():
    print("\nAt any point press R + Enter to reset the calculator.")
    saved_numbers = {}
    while True:
        first_number = get_number("First", saved_numbers)
        if first_number == "r": continue
        operator = get_operator()
        if operator == "r": continue
        second_number = get_number("Second", saved_numbers)
        if second_number == "r": continue
        result = process_calculation(first_number, operator, second_number)
        if "." in str(result) and all(char == "0" for char in str(result).rsplit(".")[-1]):
            result = int(result)
        print(f"\n{first_number} {operator} {second_number} = {result}")
        choice = get_y_or_n_choice(f"Would you like to save this number ({result})")
        if not choice:
            print("\nThis number was not saved.")
        else:
            save_letter = get_save_letter()
            if save_letter not in saved_numbers.keys():
                saved_numbers[save_letter] = result
                print(f"\n{save_letter} now equals {result}. You can use it in any calculation.")
            else:
                choice2 = get_y_or_n_choice(f"{save_letter} is already storing the"
                                            f" number {saved_numbers[save_letter]}."
                                            f"\nIt will be replaced with {result}."
                                            " Are you sure about this")
                if not choice2:
                    print("\nThis number was not saved.")
                else:
                    saved_numbers[save_letter] = result
                    print(f"\n{save_letter} now equals {result}. You can use it in any calculation.")
        next_ = input("\nPress any key + Enter to continue or Q to quit.\n")
        if next_ == "Q" or next_ == "q":
            break

print("\nWelcome to the calculator app!")
use_calculator()