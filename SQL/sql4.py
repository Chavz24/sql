# importing data to a db form csv

import csv
import sqlite3

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()

    # read the csv file and assig its data to a variable

    employees = csv.reader(open("employees.csv", mode="r"))

    # creeate a new table
    cursor.executescript(
        """ DROP TABLE IF EXISTS employees;
            CREATE TABLE employees(
                Firstname TEXT,
                Lastname TEXT
            )
        """
        )

    cursor.executemany(
        """
        INSERT INTO employees VALUES(?, ?)
        """, employees
    )
