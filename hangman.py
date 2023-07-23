from list_of_animals import animal_list

hangman = ["  +---+  ",
           "  |   |  ",
           "      |  ",
           "      |  ",
           "      |  ",
           "      |  ",
           "========="]

hangman_set = [(2 , 2, "O"), (3, 2, "|"), (3, 1, "/"), (3, 3, '\\'), (4, 1, "/"), (4, 3, '\\')]
used_letters = []


def add_letters_to_guess(word, blanked_word, letter):
    blanked_word = list(blanked_word)
    count = 0
    while count < len(word):
        if word[count] == letter:
            blanked_word[count] = letter
        count += 1
    return "".join(blanked_word)


def print_hangman(blanked_word):
    print("")
    printing = [line for line in hangman]
    side = [letter for letter in used_letters if letter not in blanked_word]
    while len(side) < 6:
        side.append(" ")
    printing[1] += f"  {side[0]}  {side[1]}"
    printing[3] += f"  {side[2]}  {side[3]}"
    printing[5] += f"  {side[4]}  {side[5]}"
    for line in printing:
        print(line)


def next_hangman_piece():
    line_as_list = list(hangman[hangman_set[0][0]])
    line_as_list[hangman_set[0][1]] = hangman_set[0][2]
    hangman[hangman_set[0][0]] = "".join(line_as_list)
    hangman_set.pop(0)


def update_guess(word, blanked_word, letter):
    if letter not in word or letter in blanked_word:
        next_hangman_piece()
        return blanked_word
    else:
        return add_letters_to_guess(word, blanked_word, letter)


def get_guess(blanked_word):
    print(f"\nWORD: {blanked_word}")
    print_hangman(blanked_word)
    while True:
        guess_letter = input("\nWhich letter? ")
        if guess_letter in used_letters:
            print("\nYou've already guessed that letter!")
        elif not guess_letter.isalpha():
            print("\nYou need to enter a letter!")
        elif len(guess_letter) != 1:
            print("\nYou must enter a single letter!")
        else:
            used_letters.append(guess_letter.lower())
            break
    print("\n\n")
    return guess_letter.lower()


print("\nWelcome to hangman!")
word = animal_list().lower()
blanked_word = "_" * len(word)
blanked_word = add_letters_to_guess(word, blanked_word, " ")
while len(hangman_set) > 0 and word != blanked_word:
    letter = get_guess(blanked_word)
    blanked_word = update_guess(word, blanked_word, letter)
if word == blanked_word:
    print(f"\nThe word was: {word}! Excellent work!")
    print_hangman(blanked_word)
    print("\nYou saved our hangman!")
else:
    print(f"\nThe word was: {word}.")
    print_hangman(blanked_word)
    print("\nOuch! Poor hangman.")