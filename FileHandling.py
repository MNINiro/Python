# 'r' : use for reading
# 'w' : use for writing
# 'x' : use for creating and writing to a new file
# 'a' : use for appending to a file
# 'r+' : use for reading and writing to the same file

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
    name = input("Enter your name:")
    FileHandle = open("sample.rtf", "w")
    FileHandle.write(Txt1)
    FileHandle.write("Nafi\n")
    FileHandle.write(name)
    FileHandle.close()
    return


def ReadText():
    FileHandle = open("sample.rtf", "r")
    # Text = FileHandle.readline()
    Text = FileHandle.read()
    print(Text)
    FileHandle.close()
    return


def AppendText():
    FileHandle = open("sample.rtf", "a")
    FileHandle.write("Ifadee\n")
    FileHandle.write("Ayman\n")
    # FileHandle.write(Txt5)
    # FileHandle.write(Txt6)
    # FileHandle.write(Txt7)
    # FileHandle.write(Txt8)
    # FileHandle.write(Txt9)
    # FileHandle.write(Txt10)
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


WriteText()
# ReadText()
# AppendText()
##ReadText()
# MultiRead()
