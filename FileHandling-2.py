def WriteText(n):
    Text = n
    FileHandle = open("E:/test.txt", "w")
    FileHandle.write(Text)
    FileHandle.write('\n')
    FileHandle.close()
    return


def ReadText():

    FileHandle = open("E:/test.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    FileHandle.close()
    return


def AppendText(m):
    Text2 = m
    FileHandle = open("E:/test.txt", "a")
    FileHandle.write(Text2)
    FileHandle.write('\n')
    FileHandle.close()
    return


def MultiLineRead():

    FileHandle = open("E:/test.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    
    while len(Text) > 0:
        Text = FileHandle.readline()
        print(Text)
    FileHandle.close()
    return


# n = str(input("Enter Data: "))
# WriteText(n)


# ReadText()

# for i in range(3):
#     m = str(input("Enter New Data:"))
#     AppendText(m)

MultiLineRead()
