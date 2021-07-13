import sqlite3
conn = sqlite3.connect('D:/test.db')

for i in range(0,2):
    IDInput = int(input("Enter ID: "))
    NameInput = str(input("Enter name: "))
    AgeInput = int(input("Enter age: "))
    AddressInput = str(input("Enter address: "))
    SalaryInput = float(input("Enter salary: "))
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (?, ?, ?, ?, ?)",
                 (IDInput, NameInput, AgeInput, AddressInput, SalaryInput))
conn.commit()
print("Records created successfully")

from DatabaseSelectQry import *
selectqry()
