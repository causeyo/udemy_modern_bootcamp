import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object -> cursor is a kind of workspace - little memory space for work
c = conn.cursor()
# execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
insert_query = '''INSERT INTO friends
                    VALUES ('Merriwether', 'Lewis', 7)'''
c.execute(insert_query)


"""
BAD WAY!

form_first = "Dana"
query = "INSERT INTO friends (first_name) VALUES ('{}')".format(form_first)
c.execute(query)
"""

# # BETTER WAY!
form_first = "Mary-Todd"
# query = "INSERT INTO friends (first_name) VALUES ({})".format('?')
query = "INSERT INTO friends (first_name) VALUES (?)"
c.execute(query, (form_first, ))

data = ("Steve", "Irwin", 9)
query1 = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query1, data)


# commit changes
conn.commit()
# "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);"
conn.close()