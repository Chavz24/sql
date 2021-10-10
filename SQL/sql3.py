import sqlite3


with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()
    cities = [
        ("Boston", "MA", 600000),
        ("Chicago", "IL", 2700000),
        ("Houston", "TX", 2100000),
        ("Phoenix", "AZ", 1500000),
    ]

    cursor.executescript(
        """ DROP TABLE IF EXISTS population;
            CREATE TABLE population(
               City TEXT,
               State TEXT,
               Population INT
            );
        """
    )
    # to run the same sql statemtn or command you can use the
    # executemany method

    # inserting multiple records using the executemany method

    cursor.executemany("""INSERT INTO population VALUES(?,?,?)""", cities)
