def get_parts():
    Parts = {
        'Case': [{'Item code': 'A1', 'Description': 'Compact', 'Price': 75},
                 {'Item code': 'A2', 'Description': 'Tower', 'Price': 150}],
        'RAM': [{'Item code': 'B1', 'Description': '8GB', 'Price': 79},
                {'Item code': 'B2', 'Description': '16GB', 'Price': 149},
                {'Item code': 'B3', 'Description': '32GB', 'Price': 299}],
        'Main HDD': [{'Item code': 'C1', 'Description': '500GB', 'Price': 49},
                     {'Item code': 'C2', 'Description': '1TB', 'Price': 89},
                     {'Item code': 'C3', 'Description': '2TB', 'Price': 159}]
    }
    return Parts


def get_total_price(Parts):
    total_price = 0
    for part in ['Case', 'RAM', 'Main HDD']:
        item_code = input(f'Enter {part} item code: ')
        found = False
        for item in Parts[part]:
            if item['Item code'] == item_code.upper():
                print(f"Selected {part}: Description: {item['Description']}, Price: {item['Price']}")
                total_price += item['Price']
                found = True
                break
        if not found:
            print(f'Item with code {item_code} not found for part {part}.')
    return total_price


def main():
    Parts = get_parts()
    total_price = get_total_price(Parts)
    print(f'Total price: {total_price}')


if __name__ == '__main__':
    main()
