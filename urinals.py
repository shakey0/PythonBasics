def get_free_urinals(urinals):
    #Have fun :)
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


print(get_free_urinals('00000'))
print(get_free_urinals('01000'))
print(get_free_urinals('1001'))
print(get_free_urinals('0'))