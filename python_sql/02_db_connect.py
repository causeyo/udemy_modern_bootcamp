import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object -> cursor is a kind of workspace - little memory space for work
c = conn.cursor()
# execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# commit changes
conn.commit()
# "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);"
conn.close()