group="Students"

studentName = input("Enter Student Name :")
studentName = studentName.upper()

if group == "Students":
      if studentName == "AKIF" or "TANISHA":
            print ("valid student")
            print("Name of the student is",studentName)
      # elif studentName == "TANISHA":
      #       print ("valid student")
      #       print("name of the student is",studentName)
      else:
            print ("Invalid Student Name")
else:
      print("Invalid group")