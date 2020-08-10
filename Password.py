def ValidatePassword(InString):
# lCaseChar, uCaseChar, numChar : INTEGER
# nextChar : CHAR
# returnFlag : BOOLEAN
# n : INTEGER

    returnFlag = TRUE
    lCaseChar = 0
    uCaseChar = 0
    numChar = 0

for n in range (0, Len(InString)):
    nextChar = InString[n]
    If nextChar > = 'a' and nextChar < = 'z':
            lCaseChar = lCaseChar + 1
        ELSE:
        IF nextChar > = 'A' and nextChar < = 'Z':
            uCaseChar = uCaseChar + 1
        ELSE:

IF nextChar > = '0' and nextChar < = '9':
    numChar = numChar + 1
ELSE:
    returnFlag = False //invalid character

IF Not (lCaseChar > = 2 and uCaseChar > = 2 and numChar > = 3):
    returnFlag = FALSE
    Return (returnFlag)

