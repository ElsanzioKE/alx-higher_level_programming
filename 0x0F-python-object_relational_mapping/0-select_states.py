#!/usr/bin/python3
"""
script that lists states in ascending order in id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    #arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # connect to the sql server
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    #create a cursor element
    cursor = connection.cursor()
    rows = cursor.fetchall()
    #dispaly results
    for row in rows:
        print(row)
    # close connection
    cursor.close()
    connection.close()

