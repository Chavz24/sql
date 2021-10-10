# inserting data to a db

import sqlite3


# using the with keyword you don't have to use the
# commit or close at the end

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()

    # executesript command executes many sql statements
    # DROP TABLE command deletes the table at the beginnig of the script
    cursor.executescript(
        """ DROP TABLE IF EXISTS population;
            CREATE TABLE population(
               City TEXT,
               State TEXT,
               Population INT
            );
            INSERT INTO population VALUES(
                'New York City',
                'NY',
                8400000
            );
            INSERT INTO population VALUES(
                'San Francisco',
                'SF',
                800000
            );
        """
    )
