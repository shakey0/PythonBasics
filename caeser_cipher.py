encrypted_words = {}
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_chars = upper_chars.lower()

def filter_word(word):
    word = list(word)
    filtered =  [char for char in word if char in upper_chars or char in lower_chars or char.isnumeric() or char == " "]
    return "".join(filtered)

def get_word():
    word = input("\nEnter the word or message you would like to encrypt.\n"
                 "(Only letters and numbers, uppercase will be converted to lowercase.)\n\nWord/Message: ")
    return filter_word(word).lower()

def get_shift_no(type_of):
    max_ = 25 if type_of == "letters" else 9
    while True:
        number = input(f"\nEnter a shift number for the {type_of}: (1 to {max_})\n")
        if not number.isnumeric():
            print("\nThat's not a number!")
        elif int(number) < 1 or int(number) > max_:
            print("\nThat's out of range!")
        else:
            return int(number)

def check_for_letter(string):
    for char in string:
        if char.isalpha():
            return True
    return False

def check_for_number(string):
    for char in string:
        if char.isnumeric():
            return True
    return False

def check_for_symbol(string):
    symbols = ["!", "@", "£", "$", "#", "%", "^", "&", "*", "?", "<", ">"]
    for char in string:
        if char in symbols:
            return True
    return False

def get_password():
    while True:
        password = input("\nEnter a password for your encrypted word or message."
                         "\n(Must contain at least 1 letter, 1 number, and 1 special character.)\n\nPassword: ")
        if len(password) < 8:
            print("\nPassword must be at least 8 characters.")
        elif not check_for_letter(password):
            print("\nPassword must contain at least 1 letter.")
        elif not check_for_number(password):
            print("\nPassword must contain at least 1 number.")
        elif not check_for_symbol(password):
            print("\nPassword must contain at least 1 symbol.")
        elif password in encrypted_words.keys():
            print("\nThis password is already in use!")
        else:
            return password

def encrypt_word(word, number, number_for_numbers):
    word = list(word)
    count = 0
    while count < len(word):
        if word[count].isnumeric():
            word[count] = int(word[count])
            word[count] += number_for_numbers
            if word[count] > 9:
                word[count] -= 10
            elif word[count] < 0:
                word[count] += 10
            word[count] = str(word[count])
        elif word[count] == " ":
            pass
        else:
            index = lower_chars.index(word[count])
            index += number if index < (26-number) else -(26-number)
            word[count] = lower_chars[index]
        count += 1
    return "".join(word)
        
def add_encrypted_word():
    word = get_word()
    number = get_shift_no("letters") if check_for_letter(word) else 1
    number_for_numbers = get_shift_no("numbers") if check_for_number(word) else 1
    password = get_password()
    encrypted_word = encrypt_word(word, number, number_for_numbers)
    encrypted_words[password] = [encrypted_word, number, number_for_numbers]
    print(f"\n\nYour encrypted word/message ---   {encrypted_word}   --- was added.\n"
           "\n\nUse the password you just gave to unencrypt it.")
    input("Press Enter to continue.")

def view_all_encrypted_words():
    print_list = ([f"{num+1}: {word[0]}" for (num, word) in zip(range(len(encrypted_words)), encrypted_words.values())])
    for item in print_list:
        print(item)

def see_encrypted_word(password):
    get_word_info = encrypted_words[password]
    word = (encrypt_word(get_word_info[0], get_word_info[1]*-1, get_word_info[2]*-1))
    print(f"\nYour message:  {word}")

def delete_encrypted_word():
    while True:
        enter_password = input("\nEnter the password for the word, or press M + Enter for the main menu.\n"
                               "\nPassword: ")
        if enter_password in encrypted_words.keys():
            confirm = input("\nAre you sure you want to delete this word/message?"
                            "\nPress Y + Enter for YES or any other key + Enter for NO.\n")
            if confirm.lower() == "y":
                encrypted_words.pop(enter_password)
                print("\nYour word/message was removed.")
            else:
                print("\nYour word/message was not removed.")
            input("\nPress Enter to continue.")
            break
        elif enter_password.lower() == "m":
            break
        else:
            print("\nPassword doesn't match any items.")

print("\nWelcome to Caeser Cipher!")
add_encrypted_word()
while True:
    print(f"\n--------------------- MAIN MENU ---------------------\n"
          f"\nYou currently have {len(encrypted_words)} encrypted words/messages."
           "\nTo view them all in their encrypted forms, press V + Enter."
           "\nTo see a specific word or message, type in its password."
           "\nTo add a new encrypted word or message, press A + Enter."
           "\nTo delete an encrypted word or message, press D + Enter."
           "\nTo exit, press Q + Enter.")
    while True:
        choice = input("\nChoose an option: ")
        if choice.lower() == "v":
            view_all_encrypted_words()
        elif choice.lower() == "a":
            add_encrypted_word()
            break
        elif choice.lower() == "d":
            delete_encrypted_word()
            break
        elif choice in encrypted_words.keys():
            see_encrypted_word(choice)
        elif choice.lower() == "q":
            exit()
        else:
            print("Invalid command.")