def last_chair(n):
    patients = []
    for number in range(n):
        patients.append(0)
    for number in range(n):
        list_of_empty = []
        empty_space = 0
        empty_space_start = 0
        empty_space_end = 0
        new_spaces = False
        for chair in patients:
            if chair == 0:
                empty_space += 1
                if not new_spaces:
                    empty_space_start = number
                    new_spaces = True
            else:
                if new_spaces:
                    empty_space_end = number - 1
                    new_spaces = False
                    list_of_empty.append([empty_space_start, empty_space_end])
        if new_spaces:
                    empty_space_end = number - 1
                    new_spaces = False
                    list_of_empty.append([empty_space_start, empty_space_end])
        largest_space = [item[1] - item[0] for item in list_of_empty]
        if len(largest_space) > 0:
            empty_area = max(largest_space)
            space = list_of_empty[largest_space.index(empty_area)]
            patient_sits = (space[0] + space[1]) // 2
            patients[patient_sits] = number + 1
        else:
            patients[0] = 1
    last_patient = max(patients)
    patient_chair = patients.index(last_patient)
    return patient_chair + 1

print(last_chair(10))