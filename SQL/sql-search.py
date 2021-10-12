"""Prompt the user whether they would like to perform an aggregation (AVG, MAX,
MIN, or SUM) or exit the program altogether."""

import sqlite3


with sqlite3.connect("newnum.db") as conn:

    cursor = conn.cursor()

    # creating a dict for the users prompt and sql queries

    promts = {
        1: "SELECT COUNT(Number) FROM nums"
    }

    cursor.execute(promts[1])

    r = cursor.fetchone()

    print(r)