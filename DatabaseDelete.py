# Delete Operation
# Following Python code shows how to use DELETE statement to delete any record and then fetch and display the remaining records from the COMPANY table.

import sqlite3

conn = sqlite3.connect('D:/test.db')
print("Opened database successfully")

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3]), "\n"

print("Operation done successfully")
conn.close()