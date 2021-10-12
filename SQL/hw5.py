"""Output the car's make and model on one line, the quantity on another line,
and then the order count on the next line."""

import sqlite3


with sqlite3.connect("cars.db") as conn:

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM inventory")

    rows = cursor.fetchall()

    for row in rows:
        print(f"Make:{row[0]} Model: {row[1]}\nQty: {row[2]}.")

        # getting the order count for the car make and model
        cursor.execute(
            "SELECT COUNT(order_date) FROM orders WHERE model=? AND make=?",
            (row[1], row[0]),
        )
        count = cursor.fetchone()

        print(f"Orders: {count[0]}")
