def gender(sex):
    if sex == 'm':
        sex = 'male'
    elif sex == "f":
        sex = 'female'
    else:
        sex = 'N'
    print(sex)
    return sex


# ====================
x = input("Enter value:")
s = gender(x)

if s == 'male':
    print('Do hardwork')
elif s == 'female':
    print('Do softwork')

# gender('m')
# gender('x')
