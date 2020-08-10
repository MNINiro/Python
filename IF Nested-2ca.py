group = input("enter group :")
if group == "student":

    age = float(input ("enter age :"))
    if age <= 16:

        gender = input("enter gender :")
        if gender == "male":
            print ("student is valid")
        else:
            print("not male")
    else:
        print("not under 16")

else:
    print("invalid group")
