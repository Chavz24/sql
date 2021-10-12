# sql functions

import sqlite3


with sqlite3.connect("new.db") as conn:

    cursor = conn.cursor()

    # creating a dict of sqlite queries

    sql = {
        "average": "SELECT AVG(population) FROM population",
        "maximum": "SELECT MAX(population) FROM population",
        "minimum": "SELECT MIN(population) FROM population",
        "sum": "SELECT SUM(population) FROM population",
        "count": "SELECT COUNT(population) FROM population",
    }
    # runnig all sql querries in the dict

    for keys, values in sql.items():
        cursor.execute(values)

        # the fecthone() record from the querry
        result = cursor.fetchone()

        print(f"{keys} population is {result[0]:.2f}")
