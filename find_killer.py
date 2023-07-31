# Given a dictionary of suspects as the keys and people they have seen as values,
# and a list of people killed, who is the killer?

def killer(suspect_info, dead):
    
    suspects = {suspect[0]: 0 for suspect in suspect_info.items()}
    
    for killed in dead:
        for people in suspect_info:
            if killed in suspect_info[people]:
                suspects[people] += 1
    
    killer = max(suspects, key=suspects.get)
    
    return killer
        
print(killer({'James': ['Jacob', 'Dave', 'Lucas', 'Sophie'], 'Johnny': ['David', 'Bill', 'Lucas', "Kyle"],
        'Peter': ['Lucy', 'Kyle', 'David'], 'Duncan': ['Jacob', 'Lucy', 'Kyle']}, ['Lucy', 'Jacob']))

