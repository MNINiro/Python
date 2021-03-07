def WriteText(p):
    Text = p
    FileHandle = open("sample.txt", "w")
    FileHandle.write(Text)
    FileHandle.close()
    return


def ReadText():

    FileHandle = open("sample.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    FileHandle.close()
    return


def AppendText(m):
    Text2 = m
    FileHandle = open("sample.txt", "a")
    FileHandle.write("\n")
    FileHandle.write(Text2)
    FileHandle.close()
    return


def MultiRead():

    FileHandle = open("sample.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    while len(Text)>0:
        Text = FileHandle.readline()
        print(Text)
    FileHandle.close()
    return

p = str(input("Enter Data:"))
WriteText(p)

ReadText()

for i in range(5):
    m = str(input("Enter Data:"))
    AppendText(m)
##    AppendText("\n")

MultiRead()
