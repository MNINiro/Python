group = "Students"

if group == "Students":
      studentName = input("Enter Student Name :")
      studentName = studentName.upper()

      if (studentName == "AKIF") or (studentName == "TANISHA"):
            print ("valid student")
            print("Name of the student is",studentName)
      else:
            print ("Invalid Student Name")
else:
      print("Invalid group")