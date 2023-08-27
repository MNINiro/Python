class Shop:
    def __init__(self, product_code, product_name, product_price):
        self.product_code = product_code
        self.product_name = product_name
        self.product_price = product_price
        self.stock = 0

    def sell_product(self, quantity):
        if quantity > self.stock:
            print(f"Insufficient stock. Only {self.stock} available.")
        else:
            self.stock = self.stock - quantity
            print(f"{quantity} {self.product_name} purchased.")

    def purchase_product(self, quantity):
        self.stock += quantity
        print(f"{quantity} {self.product_name} sold.")

    def stock_update(self, new_stock):
        self.stock += new_stock
        print(f"Stock updated. {self.stock} :{self.product_name} available.")


# -----------------------------


product = Shop("123", "Pencil", 120)
product.purchase_product(100)
product.sell_product(50)
product.stock_update(200)
