##200601 Encrypt-Decrypt

def enc(content,shift=1):
    original_ord=0
    modified_ord=0
    modified_chr=''
    encrypted_content=''
    
    for singlechr in content:
        original_ord=ord(singlechr)
        modified_ord=original_ord+shift
        modified_chr=chr(modified_ord)
        encrypted_content += modified_chr

##        above 4 line-code could be reduced to
##        the code in the following line
        
##        encrypted_content+=chr(ord(singlechr)+shift)
    return content+ ' is encrypted to '+ encrypted_content


##def ReadText():
##
##    FileHandle = open("sample.txt", "r")
##    Text = FileHandle.read()
##    print(Text)
##    print(enc(Text,2))
##    FileHandle.close()
##    return


def MultiRead():

    FileHandle = open("sample.txt", "r")
    Text = FileHandle.readline()

    print(enc(Text,2))
    
    while len(Text)>0:
        Text = FileHandle.readline()
##        print(Text)
        print(enc(Text,2))
    FileHandle.close()
    return


##ReadText()

MultiRead()
