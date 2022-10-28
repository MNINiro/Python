def timesTable(n):
    for i in range(1, 11):
        print(n, ' X ', i, ' = ', n * i)


number = int(input("What number's time table do you want to see:"))
timesTable(number)
