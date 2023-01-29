def binary_to_decimal(binary_string):
    decimal = 0
    multiplier = 1
    for digit in binary_string[::-1]:
        if digit == "1":
            decimal += multiplier
        multiplier *= 2
    return decimal


while True:
    binary_string = input("Enter a binary pattern (or leave empty to exit): ")
    if binary_string == "":
        print("Exit")
        break
    decimal = binary_to_decimal(binary_string)
    print("Decimal value:", decimal)
