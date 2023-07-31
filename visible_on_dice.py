# Supposing a dice with an even number of sides it thrown
# The numbers of the dice are always opposites of lowest-highest (1-6, 2-5, 3-4)
# Given that the bottom side is not visible, how many dots can be seen according to the top side?

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

print(total_amount_visible(5, 8))