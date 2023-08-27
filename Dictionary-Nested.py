# Define a dictionary to store the details of the parts
Parts = {
    'Case': [{'Item code': 'A1', 'Description': 'Compact', 'Price': 75},
             {'Item code': 'A2', 'Description': 'Tower', 'Price': 150}],
    'RAM': [{'Item code': 'B1', 'Description': '8GB', 'Price': 79},
            {'Item code': 'B2', 'Description': '16GB', 'Price': 149},
            {'Item code': 'B3', 'Description': '32GB', 'Price': 299}],
    'Main HDD': [{'Item code': 'C1', 'Description': '1TB', 'Price': 49},
            {'Item code': 'C2', 'Description': '2TB', 'Price': 89},
            {'Item code': 'C3', 'Description': '4TB', 'Price': 129}]
}
# '''
# Prompt the user to enter an item code
item_code = input('Enter the item code you want to check: ')

# Initialize a variable to keep track of whether the item was found or not
found = False

# Iterate over all parts and items in the dictionary
for part, items in Parts.items():
    for item in items:
        # Check if the current item has the entered item code
        if item['Item code'] == item_code.upper():
            # If the item is found, display its details and set found to True
            print(f"Item found: Part: {part}, Description: {item['Description']}, Price: {item['Price']}")
            found = True
            break
    # If the item was found, exit the outer loop as well
    if found:
        break

# If the item was not found, display a message indicating that it was not found
if not found:
    print(f'Item with code {item_code} not found in the dictionary.')
# '''











# ==============================
'''
# Initialize a variable to store the total price
total_price = 0

# Iterate over the parts for which the user needs to enter an item code
for part in ['Case', 'RAM', 'Main HDD']:
    # Prompt the user to enter an item code for the current part
    item_code = input(f'Enter {part} item code: ')

    # Initialize a variable to keep track of whether the item was found or not
    found = False

    # Iterate over the items for the current part
    for item in Parts[part]:
        # Check if the current item has the entered item code
        if item['Item code'] == item_code.upper():
            # If the item is found, display its details, add its price to the total price, and set found to True
            print(f"Selected {part}: Description: {item['Description']}, Price: {item['Price']}")
            total_price += item['Price']
            found = True
            break

    # If the item was not found, display a message indicating that it was not found
    if not found:
        print(f'Item with code {item_code} not found for part {part}.')

# Display the total price
print(f'Total price: {total_price}')
'''