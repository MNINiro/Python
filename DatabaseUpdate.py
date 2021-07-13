# Update Operation
# Following Python code shows how to use UPDATE statement to update any record and then fetch and display the updated records from the COMPANY table.

import sqlite3
conn = sqlite3.connect('D:/test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 2")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

from DatabaseSelectQry import *
selectqry()

