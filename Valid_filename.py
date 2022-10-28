def GetValidFilename():
    filename = input("Enter a filename:")
    length = len(filename)
    valid = True

    if length < 4 or length > 10:
        valid = False
        return valid
    else:
        index = 1
        while index < length and valid:
            nextChar = filename[index]
            if ('0' <= nextChar <= '10') or (
                    'a' <= nextChar <= 'z') or (
                    'A' <= nextChar <= 'Z'):
                return valid
            else:
                filename = input("Enter a filename:")

    return valid

print(GetValidFilename())