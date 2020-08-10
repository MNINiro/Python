class Parent:
    def print_last_name(self):
        print('Roberts')


class Child(Parent):
    def print_first_name(self):
        print('jason')

    def print_last_name(self): # this function overwrite Parent's last name
        print('fox')


boy = Child()
boy.print_first_name()
boy.print_last_name()