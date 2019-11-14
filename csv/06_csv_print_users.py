""""
print_users() # None
# prints to the console:
# Colt Steele
"""
from csv import DictReader


def print_users():
    with open('users.csv') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            print("{} {}".format(row['First Name'], row['Last Name']))
