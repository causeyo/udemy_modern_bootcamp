"""
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
"""


from csv import reader, writer


def update_users(first, last, new_first, new_last):
    with open('users.csv') as file:
        user_list = list(reader(file))
        users_matched = sum([1 for user in user_list if user == [first, last]])
        new_user_list = [elem if elem != [first, last] else [new_first, new_last] for elem in user_list]

    if users_matched:
        with open('users.csv', "w") as file:
            csv_writer = writer(file)
            for user in new_user_list:
                csv_writer.writerow(user)

    return "Users updated: {}.".format(users_matched)


"""
udemy solution

import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)
"""