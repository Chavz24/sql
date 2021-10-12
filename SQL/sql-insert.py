"""Add 100 random integers, ranging from 0 to 100, to a new database called
newnum.db."""

import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as conn:

    cursor = conn.cursor()

    cursor.executescript(
        """
        DROP TABLE IF EXISTS nums;
        CREATE TABLE nums(Number INT);
        """
    )

    for i in range(100):
        interger = (randint(0, 100),)

        cursor.execute("INSERT INTO nums VALUES(?)", interger)
