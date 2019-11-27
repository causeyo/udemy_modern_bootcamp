import sqlite3


conn = sqlite3.connect("users.db")
c = conn.cursor()

u = input("please enter your username...")
p = input("please enter your password...")

"""
# first of all we have to create this db
c.execute("CREATE TABLE users (username TEXT, password TEXT);")

people = [
    ("Colt", "K9nhV_as8nas1&&s"),
    ("Leslie", "2_4_xdX"),
    ("Blue", "Meow")]

c.executemany("INSERT INTO users VALUES (?,?)", people)
"""

# BAD WAY!
# query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(u, p)
# c.execute(query)
#
# this is not a good idea because we can omit password by typing ->' OR 1=1--
# two dashes(--) in SQL syntax is comment, so last quote is ignored, in result our command looks
# query = "SELECT * FROM users WHERE username='{}' AND password=''OR 1=1 --'"

# MUCH SAFER WAY is:
query = "SELECT * FROM users WHERE username=? AND password=?"
c.execute(query, (u, p))


result = c.fetchone()
if result:
    print('WELCOME BACK')
else:
    print('LOGIN FAILED')

conn.commit()
conn.close()
