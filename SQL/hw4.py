import sqlite3


with sqlite3.connect("cars.db") as conn:

    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT make FROM orders")
    makes = cursor.fetchall()

    # prints the count of every order by make
    for make in makes:
        cursor.execute(
            "SELECT COUNT(order_date) FROM orders WHERE make =?", make
            )

        make_results = cursor.fetchone()

        print(f"Make: {make[0]}\nNo. of orders:{make_results[0]}")

        cursor.execute("SELECT DISTINCT model FROM orders WHERE make=?", make)
        models = cursor.fetchall()

        # prints the count of every order by model
        for model in models:
            cursor.execute(
                "SELECT COUNT(order_date) FROM orders WHERE model =?", model
                )
            model_results = cursor.fetchone()
            print(f"Model: {model[0]}. No. of orders {model_results[0]}.")
