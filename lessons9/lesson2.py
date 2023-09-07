import mysql.connector

# conn = mysql.connector.connect(host='mysql')
# cursor = conn.cursor()
# cursor.execute('CREATE DATABASE python_db')

conn = mysql.connector.connect(host='mysql', user='admin', password='password', database='python_db')
cursor = conn.cursor()

# cursor.execute('CREATE TABLE persons(id int NOT NULL AUTO_INCREMENT, name varchar(14) NOT NULL, PRIMARY KEY(id))')

cursor.execute('INSERT INTO persons(name) values("Mike")')

conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
cursor.execute('DELETE FROM persons WHERE name = "Michel"')

cursor.close()
conn.close()