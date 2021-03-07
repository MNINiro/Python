# the file name
FileNameIn = 'Hexdata.dat'

# create a file object: open it with "write" mode
HexFile = open(FileNameIn,"w")

for line in HexFile:
    HexFile.write(Binary(line))

HexFile.close()



##def ConvertFile():
##  FileNameIn = 'Hexdata.dat'
##  HexFile = open(FileNameIn, 'r')
##  for Line in HexFile:
##    print (Line)
##    print (Binary(Line))
##  HexFile.close()
##  
