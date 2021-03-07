import sqlite3
conn = sqlite3.connect('e:/test.db')

for i in range(0, 2):
    IDInput = int(input("Enter the ID: "))
    NameInput = str(input("Enter the name: "))
    AgeInput = int(input("Enter the age: "))
    AddressInput = str(input("Enter the address: "))
    SalaryInput = float(input("Enter salary: "))
    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
                  VALUES ({}, {}, {}, {}, {})".format(IDInput, NameInput, AgeInput, AddressInput, SalaryInput))

conn.commit()
print("Records created successfully")

for row in conn.execute("SELECT id, name, age, address, salary FROM COMPANY"):
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4]), "\n"

conn.close()