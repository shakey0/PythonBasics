dict_ = {"a":4, "b":8, "c":15, "d":2}

print(max(dict_.values()))

getting = list(dict_.keys())[list(dict_.values()).index(15)]

print(getting)

my_list = [2, 5, 2, 7, 5, 2]

print(my_list.count(2))

print(6.5 - 6.1)

print(round(6.5 - 6.1, 2))

result = 6.0

if "." in str(result) and all(char == "0" for char in str(result).rsplit(".")[-1]):
    result = int(result)
    print(result)
else:
    print(f"{result} unchanged")