# #=== Ex-1 ===
class Mobile:

    @staticmethod
    def showModel():
        print('Samsung')

# x = Mobile()
# x.showModel()
Mobile.showModel()

# #=== Ex-2 ===
class Mobile1:
    fp = 'yes'      #class variable

    @staticmethod
    def showModel():
        print('Finger Print:',Mobile1.fp) #here, class name must be used to access to variable

# x = Mobile1()
Mobile1.showModel()

#=== Ex-3 === Static method with parameter
class Mobile1:

    @staticmethod
    def showModel(m,p):
        model = m
        price = p
        print(f'Model of the phone is {m} and the price is {p}')

# x = Mobile1()
Mobile1.showModel('iPhone',60000)
