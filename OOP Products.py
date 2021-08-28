class Product:
   def __init__(self):
      self.__maxprice = 1000
      self.__minprice = 1

   def sellingPrice(self):
      print('Our product maximum price is: {}'.format(self.__maxprice))
      print('Our product minimum price is: {}'.format(self.__minprice))

   def productMaxPrice(self, price):
      self.__maxprice = price

   def productMinPrice(self, price):
      self.__minprice = price

prod1= Product() #create instance
prod1.sellingPrice()

print()
prod1.__maxprice = 1500 #It will not replace the original maxprice
print('prod1.__maxprice :', prod1.__maxprice)
prod1.sellingPrice()

prod1.__minprice = 10 #It will not replace the original minprice
prod1.sellingPrice()

print()
prod1.productMaxPrice(2500)  #It will replace the original maxprice
prod1.sellingPrice()

prod1.productMinPrice(100) #It will replace the original minprice
prod1.sellingPrice()
