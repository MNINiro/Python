# You specify the filename and mode ('w' fo write)
# when you call the open function . Theline of text to be written
# to the file must contain the new line character "\ n" to move
# to the next line of the text file.

LineOfText="I am in AS Level"

FileHandle = open ("SampleFile.TXT","w") 
FileHandle.write(LineOfText)  
FileHandle.close()

## You specify the filename and mode ('r' for read) when you call
## the open function .

FileHandle = open("SampleFile.TXT","r") 
LineOfText = FileHandle.readline ()
print(LineOfText)
FileHandle.close



### You specify the filename and mode ('a' for
### append) when you call the open function.

NewLineOfText="We are learning Python"

FileHandle = open ("SampleFile.TXT","a") 
FileHandle.write(NewLineOfText) 
FileHandle.close()

##
### There is no explicit EOF function . However, when a line of text
### has been read that only consists of the end-of-file marker, the line of
### text is of length 0.

FileHandle = open ("SampleFile.TXT" , "r" )
LineOfText = FileHandle.readline()
while len(LineOfText) > 0:
       LineOfText = FileHandle.readline()
       print(LineOfText)
FileHandle.close


