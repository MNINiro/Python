fname=[]
lname=[]

fn = str(input("Enter first Name :"))
ln = input("Enter last Name :")

fname.append(fn)
lname.append(ln)
print(f"{fname[0]} {lname[0]}")

fname[0] = "Hasan"
print(f"{fname[0]} {lname[0]}")



