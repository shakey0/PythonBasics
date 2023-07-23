'''
Now it's your turn. Using at least one of the four approaches to working with lists you've seen so far:

Write a function that checks whether any passwords were added on 21/03/22
Write a function that returns a list of all passwords added on 22/03/22
'''

passwords = [
    {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

def print_found_passwords_on_date(list_of_found_passwords, date):
    display_to_user = f"\nPASSWORDS FOUND ON {date}:"
    for password in list_of_found_passwords:
        display_to_user += "\n"
        for item in password:
            if item != "added_on":
                display_to_user += f"\n{item.title()}: {password[item]}"
    print(display_to_user)
    
def any_passwords_on_date(passwords, date_added):
    # return len(list(filter(lambda password: date_added in password["added_on"], passwords))) > 0
    return len([password for password in passwords if date_added in password["added_on"]]) > 0

def passwords_added_on_date(passwords, date):
    #return list(filter(lambda password: date in password["added_on"], passwords))
    found_passwords = [password for password in passwords if date in password["added_on"]]
    if len(found_passwords) > 0:
        print_found_passwords_on_date(found_passwords, date)
    return found_passwords

print(any_passwords_on_date(passwords, "21/03/22"))
print(passwords_added_on_date(passwords, "22/03/22"))

