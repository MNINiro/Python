<<<<<<< HEAD
planes = ['2 seater','4 seater','historic']
thirtymins = [100,120,300]
sixtymins = [150,200,500]

def starter():
    for i in range(len(planes)):
        planetype = str(input('enter the type of plane: '))
        if planetype in planes:
            print(calcu())
        else:
            print('invalid plane type')
    print(planetype)
    return planetype

def calcu():
    duration = str(input('enter duration of flight: '))
    if duration == '30 mins':
        price = thirtymins(planetype)
    elif duration == '60 mins':
        price = sixtymins[planetype]
    else:
        print('invalid duration option')
        calcu()

starter()
=======
planes = ['2 seater','4 seater','historic']
thirtymins = [100,120,300]
sixtymins = [150,200,500]

def starter():
    for i in range(len(planes)):
        planetype = str(input('enter the type of plane: '))
        if planetype in planes:
            print(calcu())
        else:
            print('invalid plane type')
    print(planetype)
    return planetype

def calcu():
    duration = str(input('enter duration of flight: '))
    if duration == '30 mins':
        price = thirtymins(planetype)
    elif duration == '60 mins':
        price = sixtymins[planetype]
    else:
        print('invalid duration option')
        calcu()

starter()
>>>>>>> df2eaf8... Database handling
# calcu()