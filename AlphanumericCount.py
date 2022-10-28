n = []
nn = []
code = 'A97BB2'


numeric = 0
nonNumeric = 0

for i in range(len(code)):
    if (code[i] >= chr(48)) and (code[i] <= chr(57)):
        numeric += 1
        n.append(code[i])
    else:
        nonNumeric += 1
        nn.append(code[i])

print('Number of numeric values are', numeric, ' and the values are', n)
print('Number of non-numeric values are', nonNumeric, ' and the values are', nn)



# ===============================================================================

def DLcount(code):
    numeric = 0
    nonNumeric = 0

    for i in range(len(code)):
        if (code[i] >= chr(48)) and (code[i] <= chr(57)):
            numeric += 1
            n.append(code[i])
        else:
            nonNumeric += 1
            nn.append(code[i])

    print('Number of numeric values are', numeric, ' and the values are', n)
    print('Number of non-numeric values are', nonNumeric, ' and the values are', nn)


code = input('Enter Alphanumeric value:')
code = code.upper()

DLcount(code)

# ===============================================================================

class alphaNum:
    # n = []
    # nn = []

    def __init__(self, code):
        self.numeric = 0
        self.nonNumeric = 0
        self.code = code.upper()

    def codeCount(self):
        for i in range(len(code)):
            if (code[i] >= chr(48)) and (code[i] <= chr(57)):
                self.numeric += 1
                n.append(code[i])
            else:
                self.nonNumeric += 1
                nn.append(code[i])

        print(nn)
        print('Non-numeric values:', self.nonNumeric)
        print(n)
        print('Numeric values:', self.numeric)


code = input('Enter Alphanumeric value:')
alpNum = alphaNum(code)
alpNum.codeCount()

