import sqlite3


with sqlite3.connect("cars.db") as conn:

    cursor = conn.cursor()

    cursor.executescript(
        """
        DROP TABLE IF EXISTS orders;
        CREATE TABLE  orders
        (Make TEXT, Model TEXT, order_date TEXT)
        """
    )

    # insert 3 orders for eact model with separate order_date

    orders = [
        ("Toyota", "Tundra", "2020-12-24"),
        ("Toyota", "Tundra", "2021-12-01"),
        ("Toyota", "Tundra", "2019-24-24"),
        ("Toyota", "Tundra", "2022-24-24"),
        ("Toyota", "Corolla", "2014-05-18"),
        ("Toyota", "Corolla", "2017-03-15"),
        ("Toyota", "Corolla", "2015-04-11"),
        ("Toyota", "Accord", "2015-07-11"),
        ("Toyota", "Accord", "2015-08-11"),
        ("Toyota", "Accord", "2015-01-11"),
        ("Nissan", "R-34", "2006-03-19"),
        ("Nissan", "R-34", "2010-03-19"),
        ("Nissan", "R-34", "2012-01-19"),
        ("Nissan", "Sentra", "2020-08-22"),
        ("Nissan", "Sentra", "2020-10-23"),
        ("Nissan", "Sentra", "2020-11-26"),
    ]

    cursor.executemany("INSERT INTO orders VALUES(?,?,?)", orders)

    # ouput the make, model and qty in diferent lines and the orders below

    cursor.execute(
        """ SELECT
            inventory.make,
            inventory.model,
            inventory.quantity,
            orders.order_date
            FROM inventory, orders
            WHERE inventory.model = orders.model
        """
    )

    rows = cursor.fetchall()
    c = 0
    model = ""
    for row in rows:
        # print only the order_dates for each model until the model is changes
        if model == row[1]:
            print(f"Order_date: {row[3]}")
            model = row[1]
        else:
            c += 1
            print(f"\n{c}-Make: {row[0]} Model: {row[1]}")
            print(f"Quantity: {row[2]}")
            print(f"Order_date: {row[3]}")
            model = row[1]
