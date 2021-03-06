# adding a new table to new.db

import sqlite3


with sqlite3.connect("new.db") as conn:

    cursor = conn.cursor()

    # creating new table

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS regions
        (city TEXT, region TEXT)
        """
    )

    cities = [
        ("New York City", "Northeast"),
        ("San Francisco", "West"),
        ("Chicago", "Midwest"),
        ("Houston", "South"),
        ("Phoenix", "West"),
        ("Boston", "Northeast"),
        ("Los Angeles", "West"),
        ("Houston", "South"),
        ("Philadelphia", "Northeast"),
        ("San Antonio", "South"),
        ("San Diego", "West"),
        ("Dallas", "South"),
        ("San Jose", "West"),
        ("Jacksonville", "South"),
        ("Indianapolis", "Midwest"),
        ("Austin", "South"),
        ("Detroit", "Midwest"),
    ]

    # inserting values

    cursor.executemany("INSERT INTO regions VALUES(?,?)", cities)

    # using the ODER BY and ASC statements to fecth data in alphabetical order

    cursor.execute("SELECT * FROM regions ORDER BY region ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1])
