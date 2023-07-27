
def make_secret_key(key):
    alphabet = [chr(n) for n in range(97, 123)]
    alphabet.sort(reverse=True)
    key = list(key)
    
    key_order = []
    for char in key:
        if char not in key_order:
            key_order.append(char)
    return key_order + [letter for letter in alphabet if letter not in key_order]
    
    
def encode_or_decode(key, message, do="encode"):
    secret_key = make_secret_key(key)
    coded_message = []
    for char in message:
        coded_letter = chr(65 + secret_key.index(char)) if do!="decode" else secret_key[ord(char) - 65]
        coded_message.append(coded_letter)
    return "".join(coded_message)

print("")

print("\nFirst input to ENcode:")
print("Original string = sammylovesfightingzebrasinthebush\n" + "ENCODED string = " +
      encode_or_decode("fantasticfantasy", "sammylovesfightingzebrasinthebush") + "\n")
print("Second input to DEcode:")
print("Encoded string = EBRRHSQLXEAFWVDFCWIXZNBEFCDVXZMEV\n" + "DECODED string = " +
      encode_or_decode("fantasticfantasy", "EBRRHSQLXEAFWVDFCWIXZNBEFCDVXZMEV", "decode") + "\n")

print("\nFirst input to ENcode:")
print("Original string = ittakesmanyyearstobewise\n" + "ENCODED string = " +
      encode_or_decode("fantasticfantasy", "ittakesmanyyearstobewise") + "\n")
print("Second input to DEcode:")
print("Encoded string = FDDBTXERBCHHXBNEDQZXKFEX\n" + "DECODED string = " +
      encode_or_decode("fantasticfantasy", "FDDBTXERBCHHXBNEDQZXKFEX", "decode") + "\n")

print("")
