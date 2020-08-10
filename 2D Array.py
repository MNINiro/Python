people=[
    [1,"Gold",9.21,"USA"],
    [2,"Silver",9.56,"JAM"],
    [3,"Bronze",10.01,"GBR"]
    ]

for indArray in people:
    print(indArray)

choice=int(input("Please choose someone from the list :"))

if choice==1:
    print(people[0])
elif choice==2:
    print(people[1])
else:
    print(people[2])
    
