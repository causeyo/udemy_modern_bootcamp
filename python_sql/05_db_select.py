# it requires

import sqlite3
conn = sqlite3.connect("players.db")

c = conn.cursor()
# c.execute("SELECT * FROM players")
# c.execute("SELECT * FROM players WHERE first_name IS 'JJ'")
c.execute("SELECT * FROM players WHERE age > 20 ORDER BY age")


# it returns cursor object

for result in c:
    print(result)

# print(c.fetchall())
# it returns list of all results

# print(c.fetchone())
# it returns one row - first match

# commit changes
conn.commit()
conn.close()