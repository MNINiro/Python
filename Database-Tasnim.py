import sqlite3
conn = sqlite3.connect('e:/test.db')  # Connect To Database
print("Opened database successfully")

def name(IDInput):
    NameInput = str(input("Enter the Name to be changed: "))
    conn.execute(f"UPDATE COMPANY set NAME = '{NameInput}' where ID = {IDInput}")
    conn.commit()

def age():
    AgeInput = int(input("Enter the age to be updated: "))
    conn.execute("UPDATE COMPANY set AGE = {} where ID = {}".format(AgeInput, IDInput))
    conn.commit()

def address():
    AddressInput = str(input("Enter the address to be altered: "))
    conn.execute("UPDATE COMPANY set ADDRESS = {} where ID = {}".format(AddressInput, IDInput))
    conn.commit()

def salary():
    SalaryInput = float(input("Enter the amount to be updated: "))
    conn.execute("UPDATE COMPANY set SALARY = {} where ID = {}".format(SalaryInput, IDInput))
    conn.commit()

choice = str(input("Enter the data to be changed: Name, Age, Address, Salary ....: "))
IDInput = int(input("Enter the ID number corresponding to your choice that you wish to change: "))

if choice == 'Name':
    name(IDInput)
elif choice == 'Age':
    age(IDInput)
elif choice == 'Address':
    address(IDInput)
elif choice == 'Salary':
    salary(IDInput)
else:
    print("Error! Nothing has been updated")

print("Total number of rows updated : ", conn.total_changes)

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4]), "\n"

print("Operation done successfully")
conn.close()