# def WriteText(n):
#     Text = n
# ##    FileHandle = open("C:/Users/mnini/Documents/sample.txt", "w")
#     FileHandle = open("D:/sample.txt", "w")
#     FileHandle.write(Text)
#     FileHandle.write('\n')
#     FileHandle.close()
#     return


def ReadText():

    FileHandle = open("D:/sample.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    FileHandle.close()
    return


def AppendText(m):
    Text2 = m
    FileHandle = open("D:/sample.txt", "a")
    FileHandle.write(Text2)
    FileHandle.write('\n')
    FileHandle.close()
    return


def MultiLineRead():

    FileHandle = open("D:/sample.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    
    while len(Text)>0:
        Text = FileHandle.readline()
        print(Text)
    FileHandle.close()
    return


# n = str(input("Enter Data: "))
# WriteText(n)

ReadText()

# for i in range(2):
#     m = str(input("Enter Data:"))
#     AppendText(m)

# MultiLineRead()
