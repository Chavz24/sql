# joining adata from multiple tables

from os import curdir
import sqlite3

with sqlite3.connect("new.db") as conn:

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT population.city, population.population,regions.region
        FROM population, regions WHERE population.city = regions.city
        ORDER BY regions.city ASC
        """
    )

    rows = cursor.fetchall()

    for row in rows:
        print(f"City: {row[0]}")
        print(f"Population: {row[1]}")
        print(f"Region: {row[2]}\n")
