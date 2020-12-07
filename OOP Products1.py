class Product:

   def __init__(self):
      self.maxprice = 1000
      self.minprice = 1

   def sellingPrice(self):
      print('Our product maximum price is: {}'.format(self.maxprice))
      print('Our product minimum price is: {}'.format(self.minprice))

   def productMaxPrice(self, price):
      self.maxprice = price

   def productMinPrice(self, price):
      self.minprice = price

prod1= Product() #create instance
prod1.sellingPrice()

prod1.maxprice = 1500 #It will replace the original maxprice
# print('prod1.maxprice :', prod1.maxprice)
prod1.sellingPrice()

prod1.minprice = 10 #It will replace the original minprice
prod1.sellingPrice()

prod1.productMaxPrice(2500)  #It will replace the original maxprice
prod1.sellingPrice()

prod1.productMinPrice(100) #It will replace the original minprice
prod1.sellingPrice()