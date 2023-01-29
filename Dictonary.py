classmates = {  # 'key' : 'value'
    'Rony': ' is very curious',
    'Emma': ' is cool but talkative',
    'Sadi': ' asks too many questions',
    'Ahmed': ' is very sleepy',
    'Tamima': ' is very hard-working'
}

# print(classmates)
# print()

# for key in classmates:
#     print(key)
# print()

# print(classmates.items())

# for key, val in classmates.items():
#     print(key + val)

found = False

while not found:
    name = input('Enter Name:')

    for key, val in classmates.items():
        if key == name:
            found = True
            print(key + val)

    if not found:
        print('Name not found')
