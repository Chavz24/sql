# insert 5 records to the inventory table in car.db

import sqlite3

with sqlite3.connect("cars.db") as conn:

    cursor = conn.cursor()

    records = [
        ("Toyota", "Tundra", 345),
        ("Toyota", "Corolla", 543),
        ("Toyota", "Accord", 234),
        ("Nissan", "R-34", 200),
        ("Nissan", "Sentra", 145),
    ]

    # inserting records to the table

    # cursor.executemany("INSERT INTO inventory VALUES(?,?,?)", records)

    # updating records

    cursor.executescript(
        """
        UPDATE inventory SET quantity = 245 WHERE Model = 'Tundra';
        UPDATE inventory SET quantity = 100 WHERE Model = 'R-34';
        """
    )

    # ouput vehicles from toyota

    cursor.execute("SELECT * from inventory WHERE make= 'Toyota'")

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1], row[2])
