import psycopg2
from psycopg2 import Error
try:
	connection = psycopg2.connect(user = "postgres",password = "ammaappa123.",host = "127.0.0.1",port = "5432",database = "login")
	cursor = connection.cursor()
	create_table_query = '''CREATE TABLE login (username TEXT,password TEXT,name TEXT,email TEXT); '''
	
	cursor.execute(create_table_query)
	connection.commit()
	print("Table created successfully in PostgreSQL ")
except:
	print("Error while creating PostgreSQL table")
finally:
	#closing database connection.
	if(connection):
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")