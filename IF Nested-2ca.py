#=============================================
# group = input("enter group name :")
# if group == "student":      #if variable == value is True
#     print('Valid group')
# else:
#     print("invalid group")
#
#
# age = float(input ("enter age :"))
# if (age >= 10) and (age <= 16):
#     print("Correct age")
# else:
#     print("Invalid age")
#
#
# gender = input("enter gender :")
# if gender == "male":
#     print ("student is valid for boys fotball team")
# else:
#     print("not male")

#=============================================

group = input("enter group name :")
if group == "student":      #if variable == value is True
    print('Valid group')

    age = float(input("enter age :"))
    if (age >= 10) and (age <= 16):
        print("Correct age")

        gender = input("enter gender :")
        if gender == "male":
            print('student is valid for boys football team')
        elif gender == "female":
            print('student is valid for girls football team')
        else:
            print("not a valid gender")
    else:
        print("Invalid age")
else:
    print("invalid group")

