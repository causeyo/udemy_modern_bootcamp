import sqlite3


conn = sqlite3.connect("players.db")
c = conn.cursor()
c.execute("CREATE TABLE players (first_name TEXT, last_name TEXT, age INTEGER);")


people = [
    ("Robert", "Lewandowski", 31),
    ("JJ", "Okocha", 46),
    ("Antoine", "Griezmann", 28),
    ("Ansu", "Fati", 17),
    ("Lionel", "Messi", 32),
    ("Cristiano", "Ronaldo", 34)]

# c.executemany("INSERT INTO players VALUES (?,?,?)", people)

average = 0
for person in people:
    c.execute("INSERT INTO players VALUES (?,?,?)", person)
    average += person[2]
print(average/len(people))

"""it is equal to:
for person in people:
    c.execute("INSERT INTO players VALUES (?,?,?)", people")
    average += person[2]
print(average/len(people))

"""

# commit changes
conn.commit()
conn.close()
