"""
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
"""
from csv import DictWriter


def add_user(first_name, last_name):
    with open("users.csv", "a") as file:
        headers = ["First Name", "Last Name"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            "First Name": first_name,
            "Last Name": last_name,
        })


"""
udemy solution

import csv
 
def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])
"""