"""
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
"""


from csv import reader, writer


def delete_users(first, last):
    with open('users.csv') as file:
        user_list = list(reader(file))
        users_matched = sum([1 for user in user_list if user == [first, last]])
        new_user_list = [elem for elem in user_list if elem != [first, last]]

    if users_matched:
        with open('users.csv', "w") as file:
            csv_writer = writer(file)
            for user in new_user_list:
                csv_writer.writerow(user)

    return "Users deleted: {}.".format(users_matched)

"""
udemy solution

import csv
 
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users deleted: {}.".format(count)
"""