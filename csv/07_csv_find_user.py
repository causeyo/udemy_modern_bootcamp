"""
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
"""


from csv import reader


def find_user(first, last):
    with open('users.csv') as file:
        csv_reader = list(reader(file))
        for user in csv_reader:
            if user[0]==first and user[1]==last: return csv_reader.index(user)
        return "{} {} not found.".format(first, last)
