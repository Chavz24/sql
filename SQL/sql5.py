# retrieving data from a db.

import sqlite3

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()

    # using a for loop to print the db line by line

    cursor.execute("SELECT firstname, lastname FROM employees")

    # the fecthall() statement retrieves all records from the querry

    rows = cursor.fetchall()

    # print the row one by one on console

    for row in rows:
        print(row[0], row[1])
