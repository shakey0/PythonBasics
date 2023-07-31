# Given a list of 0s and 1s with 0s representing free urinals and 1 representing taken urinals,
# and the fact that people coming in will not dare use a urinal next to one that is already taken,
# how many urinals are actually free

def get_free_urinals(urinals):
    urinals_list = [char for char in urinals]
    used = 0
    for char in urinals_list:
        if char == '1':
            used += 1
            if used == 2:
                return -1
        else:
            used = 0
    if len(urinals_list) == 1:
        if urinals_list == ['0']:
            return 1
        else:
            return 0
    counter = 1
    if urinals_list[0] == urinals_list[1] == '0':
        urinals_list[0] = '1'
    while counter < len(urinals_list)-1:
        if urinals_list[counter] == urinals_list[counter-1] == urinals_list[counter+1] == '0':
            urinals_list[counter] = '1'
        counter += 1
    if urinals_list[-1] == urinals_list[-2] == '0':
        urinals_list[-1] = '1'
    return urinals_list.count('1') - urinals.count('1')

print("Result Error:  " + str(get_free_urinals('11000')))
print("Result 1:  " + str(get_free_urinals('00000')))
print("Result 2:  " + str(get_free_urinals('01000')))
print("Result 3:  " + str(get_free_urinals('00010')))
print("Result 4:  " + str(get_free_urinals('1001')))
print("Result 5:  " + str(get_free_urinals('0')))
print("Result 6:  " + str(get_free_urinals('000000')))
print("Result 7:  " + str(get_free_urinals('0000000')))
print("Result 8:  " + str(get_free_urinals('0010010')))
print("Result 9:  " + str(get_free_urinals('10000')))
print("Result 10:  " + str(get_free_urinals('00100')))
print("Result 11:  " + str(get_free_urinals('00001')))