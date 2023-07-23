def total_amount_visible(top_num, num_of_sides):
    all_sides = []
    counter = 1
    while counter <= num_of_sides:
        all_sides.append(counter)
        counter += 1
    all_sides_rev = []
    counter = num_of_sides
    while counter > 0:
        all_sides_rev.append(counter)
        counter -= 1
    total_sum = 0
    for num in all_sides:
        total_sum += num
    index_of = all_sides.index(top_num)
    total_sum -= all_sides_rev[index_of]
    return total_sum

list_of_empty = [[4, 5], [3, 2], [9, 4]]

largest_space = [item[1] - item[0] for item in list_of_empty]

print(largest_space)