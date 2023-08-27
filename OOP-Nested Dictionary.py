class Part:
    def __init__(self, item_code, description, price):
        self.item_code = item_code
        self.description = description
        self.price = price

class ComputerParts:
    def __init__(self):
        self.parts = {
            'Case': [Part('A1', 'Compact', 75), Part('A2', 'Tower', 150)],
            'RAM': [Part('B1', '8GB', 79), Part('B2', '16GB', 149), Part('B3', '32GB', 299)],
            'Main HDD': [Part('C1', '500GB', 49), Part('C2', '1TB', 89), Part('C3', '2TB', 159)]
        }

    def get_part(self, part_name, item_code):
        if part_name in self.parts:
            for part in self.parts[part_name]:
                if part.item_code == item_code.upper():
                    return part
        return None

    def calculate_total_price(self, selected_parts):
        total_price = 0
        for part_name, item_code in selected_parts.items():
            part = self.get_part(part_name, item_code)
            if part:
                total_price += part.price
        return total_price

def main():
    computer_parts = ComputerParts()
    selected_parts = {}
    for part_name in ['Case', 'RAM', 'Main HDD']:
        item_code = input(f'Enter {part_name} item code: ')
        part = computer_parts.get_part(part_name, item_code)
        if part:
            print(f"Selected {part_name}: Description: {part.description}, Price: {part.price}")
            selected_parts[part_name] = item_code
        else:
            print(f'Item with code {item_code} not found for part {part_name}.')
    total_price = computer_parts.calculate_total_price(selected_parts)
    print(f'Total price: {total_price}')

if __name__ == '__main__':
    main()
