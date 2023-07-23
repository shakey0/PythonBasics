def waterbombs(fire, w):
    fire_count = 0
    water_needed = 0
    in_fire = False
    for item in fire:
        if item == "x":
            fire_count += 1
            in_fire = True
        else:
            if in_fire:
                water_needed += 1
                fire_count = 0
            in_fire = False
        if fire_count == w:
            water_needed += 1
            fire_count = 0
            in_fire = False
    if fire_count > 0:
        water_needed += 1
    return water_needed

print(waterbombs('xYxxxxxxYYxYxxx', 3))