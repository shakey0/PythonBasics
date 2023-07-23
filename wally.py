def wheres_wally(string):
    list_of_words = string.split()
    wally = False
    for item in list_of_words:
        if "Wally" in item:
            wally = True
            break
    if not wally:
        return -1
    where = string.index("Wally")
    if string[where-1] != " " and where != 0:
        return -1
    if string[where+5].isalpha():
        return -1
    return where

print(wheres_wally("Wally!"))