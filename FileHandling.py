# 'r' : use for reading
# 'w' : use for writing
# 'x' : use for creating and writing to a new file
# 'a' : use for appending to a file
# 'r+' : use for reading and writing to the same file
# FileHandle.write("Nafi\n")
#

Txt1 = "1 2 3 4 5 \n"
Txt2 = "6 7 8 9 10 \n"
Txt3 = "11 12 13 14 15 \n"
Txt4 = "16 17 18 19 20 \n"
Txt5 = "21 22 23 24 25 \n"
Txt6 = "26 27 28 29 30 \n"
Txt7 = "31 32 33 34 35 \n"
Txt8 = "36 37 38 39 40 \n"
Txt9 = "41 42 43 44 45 \n"
Txt10 = "46 47 48 49 50 \n"


def WriteText():
    FileHandle = open("d:\sample.txt", "w")
    # name = input("Enter your name:")
    # FileHandle.write(name)
    # FileHandle.write("\n")
    FileHandle.write(Txt4)
    FileHandle.close()
    return



def ReadText():
    FileHandle = open("d:\sample.txt", "r")
    Text = FileHandle.readline()
    # Text = FileHandle.read()
    print(Text)
    FileHandle.close()
    return


def AppendText():
    FileHandle = open("d:\sample.txt", "a")
    FileHandle.write("Ifadee\n")
    FileHandle.write("Ayman\n")
    FileHandle.close()
    return

def MultiRead():
    FileHandle = open("sample.txt", "r")
    Text = FileHandle.readline()
    print(Text)
    while len(Text) > 0:
        Text = FileHandle.readline()
        print(Text)
    FileHandle.close()
    return


# WriteText()
# AppendText()
ReadText()
# MultiRead()
