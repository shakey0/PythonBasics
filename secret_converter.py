conversion_dict = {
    'A': 'n', 'B': '1', 'C': 'Y', 'D': 'g', 'E': '5', 'F': 'L', 'G': 'b', 'H': '9', 'I': 'r', 'J': 'w',
    'K': '0', 'L': 'Q', 'M': 'u', 'N': 'D', 'O': '2', 'P': 'z', 'Q': 'H', 'R': 'S', 'S': 'e', 'T': 'T',
    'U': 'o', 'V': '3', 'W': 'm', 'X': 'F', 'Y': 'k', 'Z': 'A', 
    'a': 'V', 'b': 'j', 'c': 'X', 'd': 'E', 'e': '6', 'f': 'M', 'g': 'i', 'h': 'P', 'i': 't', 'j': 's',
    'k': 'G', 'l': 'J', 'm': '8', 'n': 'l', 'o': '4', 'p': 'B', 'q': 'Z', 'r': 'C', 's': 'q', 't': 'W',
    'u': 'd', 'v': 'I', 'w': 'K', 'x': 'R', 'y': 'p', 'z': 'v',
    '0': 'h', '1': 'c', '2': 'x', '3': 'N', '4': 'O', '5': '7', '6': 'U', '7': 'y', '8': 'a', '9': 'f'
}

print(len(conversion_dict) == 62)

for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
    if char not in conversion_dict.keys():
        print(char)
    if char not in conversion_dict.values():
        print(char)

for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    if char not in conversion_dict.keys():
        print(char)
    if char not in conversion_dict.values():
        print(char)

for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    if num not in conversion_dict.keys():
        print(num)
    if num not in conversion_dict.values():
        print(num)


name_to_convert = "Nice Company"

scrambled_name = ""
for char in name_to_convert:
    scrambled_name += conversion_dict[char] if char != " " else " "
scrambled_name = scrambled_name.replace(" ", "%20")

print(scrambled_name)

unscrambled_name = ""
scrambled_name = scrambled_name.replace("%20", " ")
for char in scrambled_name:
    unscrambled_name += [key for key, value in conversion_dict.items() if value == char][0] if char != " " else " "
print(unscrambled_name)
