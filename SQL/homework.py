import sqlite3

# create a db or a conection to a db

conn = sqlite3.connect("cars.db")

# creates a cursor to pass commands to a db

cursor = conn.cursor()

# creates table in the db using the cursor

cursor.execute(
    """CREATE TABLE IF NOT EXISTS inventory
    (Make TEXT, Model TEXT, Quantity INT)"""
)
# close the connection to the db

conn.close()
