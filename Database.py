# Create a Table
# Following Python program will be used to create a table in the previously created database.

import sqlite3

conn = sqlite3.connect('D:/test.db') #Connect To Database

print("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")

conn.close()
