#!/usr/bin/python3
# version.py – Fetch and display the MySQL database server version.
# import the MySQLdb and sys modules

# grant all on *.* to gbuser@localhost identified by 'gb5xPiys5u';
import MySQLdb
import sys
# open a database connection

# Goalboost password:  grant all on *.* to gbuser@localhost identified by 'gb5xPiys5u';


# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "192.168.1.1", user = "root", passwd = "Newacct1", db = "goalboost")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
cursor.execute ("SELECT VERSION()")
# fetch a single row using fetchone() method.
row = cursor.fetchone ()
# print the row[0]
# (Python starts the first row in an array with the number zero – instead of one)
print ("Server version:", row[0])
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
# exit the program
sys.exit()