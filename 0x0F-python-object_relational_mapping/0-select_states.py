#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <usernme> <password> <database>" .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
    except MySQLdb.Error as e:
        print("Error connecting to MysQL:", e)
        sys.exit(10)

    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        states = cursor.fetchall()
    except MySQLdb.error as e:
        print("Error executing query:", e)
        db.clode()
        sys.exit(1)

    for state in states:
        print(state)

    cursor.close()
    db.close()
