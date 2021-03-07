#Declare marks as Integer

marks = int(input("Enter marks :"))

if (marks < 0) or (marks > 100):
    print("Error!")
else:
    if marks > 80:
        print("Grade A")
    elif (marks > 60) and (marks <=80):
        print("Grade B")
    elif (marks > 40) and (marks <=60):
        print("Grade C")
    else:
        print("Fail")


# marks = int(input("Enter the marks you obtained: "))
# if marks == 100:
#     print("Outstanding")
# elif (marks == 97) or (marks == 99):
#     print("Awesome")
# elif ((marks >= 90) and (marks <= 96)) or (marks == 98):
#     print("A*")
# elif (marks >= 80) and (marks <= 89):
#     print("A")
# elif (marks >= 70) and (marks <= 79):
#     print("B")
# elif (marks >= 60) and (marks <=69):
#     print("C")
# elif (marks >=50) and (marks <= 59):
#     print("D")
# else:
#     print("Fail")


