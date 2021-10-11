# updating and deleting data from a db

import sqlite3

with sqlite3.connect("new.db") as conn:

    cursor = conn.cursor()

    # upadating data

    cursor.execute(
        """
        UPDATE population SET population = 9000000 WHERE city = 'New York City'
        """
    )

    # deleting data

    cursor.execute("""DELETE FROM population WHERE city = 'Boston'""")

    print("\nNew Data\n")

    cursor.execute("SELECT * FROM population")
    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1], row[2])
