import sqlite3

# create a db or if it does not exist
# or connects to a db if it exist
conn = sqlite3.connect("new.db")

# create a cursor to eecute sql commands

cursor = conn.cursor()

# create a table

cursor.execute(
    """CREATE TABLE IF NOT EXISTS population
    (city TEXT, state TEXT, pupulation INT)"""
)

# close the connection to db

conn.close()
