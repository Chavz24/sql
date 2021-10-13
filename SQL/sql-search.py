"""Prompt the user whether they would like to perform an aggregation (AVG, MAX,
MIN, or SUM) or exit the program altogether."""

import sqlite3
from sys import exit
from time import sleep


def calc(user_input: int):
    """This function  does the operation and returns a result"""
    cursor.execute(promts[user_input])
    result = cursor.fetchone()[0]
    return result


def outcome(user_input: int):
    """This function determines what operation the user chose"""
    if user_input == 1:
        print(f"The sum of all the number in the table is {calc(user_input)}.")
    elif user_input == 2:
        print(f"The max number in the table is {calc(user_input)}.")
    elif user_input == 3:
        print(f"The min number in the table is {calc(user_input)}.")
    else:
        print(f"The average of the numbers in table is {calc(user_input)}.")


with sqlite3.connect("newnum.db") as conn:

    cursor = conn.cursor()

    # creating a dict for the users prompt and sql queries

    promts = {
        1: "SELECT SUM(Number) FROM nums",
        2: "SELECT MAX(Number) FROM nums",
        3: "SELECT MIN(Number) FROM nums",
        4: "SELECT AVG(Number) FROM nums",
        5: None,
    }
    # menu to promt the user
    menu = """
    \nPlease seclect one the followins options:
    \n1. Add all the number in the table.
    \n2. Show the max number in the table.
    \n3. Show the min number in the table.
    \n4. Show the average of the table.
    \n5. Exit the program.
    \n>>>"""

    # infinite loop to ask the user what he would like to do.
    while True:
        try:
            user_input = int(input(menu))
            if user_input not in promts.keys():
                print("That is not a valid option.")
                sleep(1)
            elif user_input == 5:
                exit()
            else:
                outcome(user_input)
                sleep(2)
        except ValueError:
            print("That is not a valid option.")
            sleep(1)
