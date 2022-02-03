import random
import sqlite3

connection = sqlite3.connect('anekdot.db')
cursor = connection.cursor()
z = random.randrange(1, 9000, 1)
cursor.execute('SELECT * FROM anekdot WHERE rowid=' + str(z))
row = cursor.fetchone()
print(row[1])
connection.close()