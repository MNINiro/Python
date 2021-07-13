# Delete Operation
# Following Python code shows how to use DELETE statement to delete any record and then fetch and display the remaining records from the COMPANY table.
import sqlite3
conn = sqlite3.connect('D:/test.db')
print("Opened database successfully")

conn.execute("DELETE from COMPANY where ID = 1;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

from DatabaseSelectQry import *
selectqry()
