plainText = input('Enter any name:')
cypherText = ''
cypherValue = int(input('Enter Cypher value:'))

for i in range(len(plainText)):
    x = ord(plainText[i])
    y = chr(x + cypherValue)
    cypherText += y
print(plainText)
print(cypherText)
