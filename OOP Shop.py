class Shop:
    def __init__(self, product_code, product_name, price):  # constructor
        self.product_code = product_code
        self.product_name = product_name
        self.price = price
        self.stock = 0

    def sell_product(self, quantity):
        if quantity > self.stock:
            print(f"Insufficient stock. Only {self.stock} available.")
        else:
            self.stock = self.stock - quantity
            print(f"{quantity} {self.product_name} sold.")

    def purchase_product(self, quantity):
        self.stock += quantity
        print(f"{quantity} {self.product_name} purchased.")

    def stock_update(self, new_stock):
        self.stock += new_stock
        print(f"Stock updated. {self.stock} {self.product_name} available.")


# ============= MAIN BODY =================
my_shop = Shop("001", "Apple", 0.5)     # object or instance
my_shop1 = Shop("010", "Banana", 0.4)

my_shop.purchase_product(100)
my_shop.sell_product(50)
my_shop.stock_update(200)

# print(my_shop.product_code)
# print(my_shop.product_name)
# print(my_shop.price)
# print(my_shop.stock)
# print()

# print(my_shop1.product_code)
# print(my_shop1.product_name)
# print(my_shop1.price)
# print(my_shop1.stock)