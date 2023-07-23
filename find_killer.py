def killer(suspect_info, dead):
    
    suspects = {suspect: 0 for (suspect, value) in suspect_info.items()}
    
    for killed in dead:
        
        for people in suspect_info:
            
            if killed in suspect_info[people]:
                suspects[people] += 1
    
    killer = max(suspects, key=suspects.get)
    
    return killer
        
print(killer({'James': ['Jacob', 'Dave', 'Lucas'], 'Johnny': ['David', 'Bill', 'Lucas'],
        'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']))

