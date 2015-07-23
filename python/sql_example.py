# JCL todo get rid of other driver
import mysql.connector

# Todo use Goalboost user to connect
cnx = mysql.connector.connect(user='root', password='Newacct1',
                              host='127.0.0.1',
                              database='goalboost')

# Default for dictionary is false and returns a tuple. We want the keys too, so force
# use of cursor.MySQLCursorDict
cursor = cnx.cursor(dictionary = True)

# An example query
query = "select * from tasks"

try:
	cursor.execute(query)
	for row in cursor:	
		print("\n") # Separator
		for key in list(row.keys()):			
			print('{:>15}  : {}'.format(key, row[key]))  # print key right aligned, then value			
finally:
	cursor.close()
	cnx.close()