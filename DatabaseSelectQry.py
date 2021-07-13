# Select Operation
# Following Python program shows how to fetch and display records from the COMPANY table created in the above example.
def selectqry():
   import sqlite3
   conn = sqlite3.connect('D:/test.db')
   print("Opened database successfully")

   cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
   for row in cursor:
      print("ID = ", row[0])
      print("NAME = ", row[1])
      print("AGE = ", row[2])
      print("ADDRESS = ", row[3])
      print("SALARY = ", row[4]), "\n"

   print("Operation done successfully")
   conn.close()

# selectqry()