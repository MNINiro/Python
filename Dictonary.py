classmates = {  # 'key' : 'value'
    'Rony': ' is very curious',
    'Emma': ' is cool but talkative',
    'Sadi': ' asks too many questions',
    'Ahmed': ' is very sleepy',
    'Tamima': ' is very hard-working'
}
# print(classmates)
# print()

for key, val in classmates.items():
    print(key + val)








'''
found = False

while found == False:
    name = input('Enter Name:')

    for key, val in classmates.items():
        if key == name:
            found = True
            print(key + val)

    if not found:
        print('Name not found')
'''




# print()
# print(classmates.items())
#
# for val in classmates.items():
#     print(val)
# print()

# for key, val in classmates.items():
#     print(key+val)
# print()
#
# for key, val in classmates.items():
#     print(key + val)
# print()

# """


# """

'''
people = {
    1: {'name': 'John', 'age': '27', 'sex': 'Male'},
    2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
}

for key, value in people.items():
    print(f"Person {key}:")

    for k, v in value.items():
        print(f"  {k}: {v}")
'''

