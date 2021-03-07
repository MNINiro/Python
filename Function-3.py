def gender(sex):
    print(sex);
    if sex=='m':
        sex='male'

    elif sex=="f":
        sex='female'
    else:
        sex='N'

    print(sex)

#====================
x = input("Enter value:")
gender(x)

# gender('m')
# gender('x')

