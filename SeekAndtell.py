
def tellread():
    f = open("E:/test.txt", "r")
    cursor_position = f.tell()
    print("Cursor Position is :", cursor_position)

    data = f.read(5)
    print("After reading 5 data from file")
    cursor_position = f.tell()
    print("Cursor Position is :", cursor_position)

def seekread():
    f = open("E:/test.txt", "rb")
    f.seek(-10, 2)
    cursor_position = f.tell()
    print("Cursor Position is :", cursor_position)
    data = f.read().decode('utf-8')
    print(data)

# tellread()
# print()
seekread()


