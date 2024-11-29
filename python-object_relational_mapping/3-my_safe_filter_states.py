#!/usr/bin/python3
"""
A script to securely query a MySQL database for states by name.
Prevents SQL injection by using parameterized queries.
"""

import MySQLdb
import sys

def connect_and_query(database_name, state_name):
    """
    Connects to a MySQL database and fetches records securely.

    Parameters:
        database_name (str): The name of the MySQL database.
        state_name (str): The state name to search for.

    Returns:
        None
    """
    try:
        # Establish the database connection
        db = MySQLdb.connect(
            host="localhost",
            user="root",         # Replace with your MySQL username
            passwd="password",   # Replace with your MySQL password
            db=database_name
        )

        cursor = db.cursor()

        # Secure query to prevent SQL injection
        query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)  # Outputs tuples as required

    except MySQLdb.Error as error:
        print(f"Database error: {error}")

    finally:
        # Ensure the cursor and connection are properly closed
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Connect to the database and search for the provided state name
        connect_and_query("database_name", sys.argv[1])
    else:
        # Display usage information if arguments are incorrect
        print("Usage: ./main.py <state_name>")
        sys.exit(1)  # Exit to prevent further execution

