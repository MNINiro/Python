# Select Operation
# Following Python program shows how to fetch and display records from the COMPANY table created in the above example.


import sqlite3

conn = sqlite3.connect('D:/test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3]), "\n"

print("Operation done successfully")
conn.close()