import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
)
cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE IF NOT EXISTS matin")

print("All Done")