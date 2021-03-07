# # #===Ex-1===
# str = "My age is {}"
# print(str.format(60))
# print('my age is {}'.format(60))
#
# #===Ex-2===
# name = "Niro"
# age = 50
# print('My name is {} and I am {} years old'.format(name,age))
#
# # #===Ex-3===
# a = 50
# b = 3
# print("{}".format(a/b))
# print("{:.2}".format(a/b))
# print("{:.2%}".format(a/b))
#
# #===Ex-4===
# print("{:,}".format(1234567890)) #it will put comma after every thousands
# print("{:_}".format(1234567890)) #it will put # after every thousands
#
# #===Ex-5===
# print("Mobile price is {} and Computer price is {}, Total is {} ".format(20000,50000,20000+50000))

#===Ex-6 on tuple===
# value = (10,20) #tuple
# print("{0[0]} {0[1]}".format(value)) #since it's a tupel, it requires index
# print("{0[1]} {0[0]}".format(value)) #since it's a tupel, it requires index

# #===Ex-7 on dictionary===
# data1 = {'sami':2000, 'remi':3000} #Key and value
# print("{0[sami]} {0[remi]}".format(data1))
# print("{dt[sami]} {dt[remi]}".format(dt = data1))
# print("{0[sami]:d} {0[remi]:d}".format(data1)) #:d for integer but same result
# print("{sami} {remi}".format(**data1)) # "**" known as format parameter
#
# #===Ex-8=== Integer and float
# print("{}".format(10))
# print("{0}".format(10))
# print("{0} {1}".format(10,20.5)) #following index - tuple
# print("{num1}".format(num1=10))
# print("{num1} {num2}".format(num1=10.5, num2=20))
# print("{num2} {num1}".format(num1=10, num2=20))
#
# # ===Ex-9=== Strings ===
# print("{}".format("hello"))
# print("{0}".format("Hello"))
# print("{0} {1}".format("Hello","World")) #following index
# print("{str1}".format(str1="world"))
# print("{str1} {str2}".format(str1="Hi", str2="Dear"))
# print("{str1} {str2}".format(str1="Hello", str2="World"))
#
# #===Ex-10=== String and integer or float
# print("{str1} {num1}".format(str1="Price", num1=10))
# print("{str1} {num1}".format(num1=20.5, str1="taka"))
#
# #===Ex-11=== "d" format for only integer values
# print("{:d}".format(15))
# print("{0:d}".format(15))
# print("{num:d}".format(num=15))

#===Ex-12=== Format methods
# :[fill][align][sign][#][0][width][,][.precision]type
# 5d it will give 5 widths. (here, empty represented by "-" sign)
# print("{num:5d}".format(num=15)) # it will give 5 widths like, - - - 1 5 in an array
# print("{num:05d}".format(num=15)) # it will give 5 widths with 0 prefix like, 0 0 0 1 5 in an array
# print("{num:+5d}".format(num=15)) # it will give 5 widths with + sign like, + 1 5 in an array
# print("{num:<5d}".format(num=15)) # it will give 5 widths with left align like, 1 5 - - - in an array
# print("{num:>5d}".format(num=15)) # it will give 5 widths with right align like, - - - 1 5 in an array
# print("{num:*<5d}".format(num=15)) # it will give 5 widths with left align and fill with * like, 1 5 * * * in an array
# print("{num:#>5d}".format(num=15)) # it will give 5 widths with right align and fill with # like, # # # 1 5 in an array
# print("{num:*^5d}".format(num=15)) # ^ will place 5 in the middle then rest of the places will be filled up like - 1 5 - -

#===Ex-13=== floating point numbers. it will also accept integers
# print("{}".format(15.65))
# print("{:f}".format(15.65))
# print("{0:f}".format(15))
# print("{num:f}".format(num=15.65))

#===Ex-14===
# # :[fill][align][sign][#][0][width][,][.precision]type (here, empty represented by "-" sign)
# print("{num:8f}".format(num=15.65)) #8f it will give 9 widths (1 extra for decimal point.) like, 15.650000 in an array
# print("{num:8.3f}".format(num=15.65)) # in 3 precision format o/p will be - - 15.650 (8 width)
# print("{num:+8.2f}".format(num=15.85)) # in 2 precision format o/p will be - - +15.65 (8 width)
# print("{num:<8.2f}".format(num=15.95)) # left align like, 15.95 - - -
# print("{num:>8.2f}".format(num=15.66)) # right align like, - - - 1 5 in an array
# print("{num:*<8.2f}".format(num=15.88)) # left align with 2 precision and fill with * like, 15.88 * * *
# print("{num:*>8.3f}".format(num=15.55)) # right align with 3 precision and fill with # like, * * 15.550
# print("{num:*^8.2f}".format(num=15.25)) # ^ will place 15.25 in the middle then rest of the places will be filled up with * like *15.25**
# print("{num:^8.2f}".format(num=15.25)) # ^ will place 15.25 in the middle then rest of the places will be empty

#===Ex-15===
# # :[fill][align][sign][#][0][width][,][.precision]type (here, empty represented by "-" sign)
# #8s, will give 8 spaces and
# print("{:8s}".format("world")) #string will start from the left by defaut
# print("{:<8s}".format("world")) #string will start from the left
# print("{:*<8s}".format("world")) #string will start from the left then put *'s at the right
# print("{:>8s}".format("world")) #string will start from the right and leave spaces at the left
# print("{:*>8s}".format("world")) #string will start from the right and put *s at the left
# print("{:^8s}".format("world")) #string will start from the middle.
# print("{:*^8s}".format("world")) #string will start from the middle and rest of the places will be filled up by *s

#===Ex-16===
# # :[fill][align][sign][#][0][width][,][.precision]type (here, empty represented by "-" sign)
# #8s, will give 8 spaces and first 3 charecters
# print("{:.3s}".format("world")) #will start from the left by defaut
# print("{:8.3s}".format("world")) #will start from the left by defaut
# print("{:<8.3s}".format("world")) #will start from the left
# print("{:*<8.3s}".format("world")) #will start from the left then put *'s at the right
# print("{:>8.3s}".format("world")) #will start from the right and leave spaces at the left
# print("{:*>8.3s}".format("world")) #will start from the right and put *s at the left
# print("{:^8.3s}".format("world")) #will start from the middle.
# print("{:*^8.3s}".format("world")) #will start from the middle and rest of the places will be filled up by *s

#===Ex-17===
# Syntex: f"{index/key/name:[fill][align][sign][#][0][width][,][.precision]type}"
# a = 10
# b = 20
# print(f"{a}")
# print(f"Price is {a} taka")
# print(f"{a} {b}")
# print(f"{}") #in f-string empty {} is not allowed

# #===Ex-18===
# #floating values
# c = 10.55
# d = 15.45
# print(f"{d} {c} {c+d}") #adding two values

# #===Ex-19===
# fname = "Ahyaan"
# lname = "Noor"
# print(f"{fname}")
# print(f"Little boy's name is {fname} {lname}")

# #===Ex-20===
# num = 10
# print(f"{num}")
# print(f"{num:d}")
# print(f"{num:05d}")
# print(f"{num:+5d}")
# print(f"{num:<5d}")
# print(f"{num:*<5d}")
# print(f"{num:*>5d}")
# print(f"{num:^5d}")
# print(f"{num:*^5d}")

# #===Ex-21===
# num = 15.66
# price = 15.256654515
#
# print(f"{num}")
# print(f"{num:f}") #last f for float
# print(f"{num:8f}")
# print(f"{price:.20f}")
# print(f"{num:8.3f}")
# print(f"{num:+8.2f}")
# print(f"{num:<8.3f}")
# print(f"{num:*<8.3f}")
# print(f"{num:>8.3f}")
# print(f"{num:*>8.3f}")
# print(f"{num:^8.3f}")
# print(f"{num:*^8.3f}")

# #===Ex-22===
# name = "Sami"
# print(f"{name}")
# print(f"{name:s}")
# print(f"{name:8s}")
# print(f"{name:<8}")
# print(f"{name:*<8}")
# print(f"{name:>8}")
# print(f"{name:*>8s}")
# print(f"{name:^8s}")
# print(f"{name:*^8s}")

#===Ex-23===
# name = "Sami"
# print(f"{name}")
# print(f"{name:.3s}")
# print(f"{name:8.3s}")
# print(f"{name:<8.3s}")
# print(f"{name:*<8.3s}")
# print(f"{name:>8.3s}")
# print(f"{name:*>8.3s}")
# print(f"{name:^8.3s}")
# print(f"{name:*^8.3s}")

# #===Ex-24===
# price = 1234567890
# print(f"{price:,}")
# print(f"{price:_}")

# #===Ex-25===
# name = "Niro"
# age = 50
# print(f'My name is {name} and I am {age} years old')
#
# #===Ex-26===
# print(f"{10*5}")
#
# a = 50
# b = 3
# print((f"{a/b:.2}"))
# print((f"{a/b:.2%}"))

# #===Ex-27=== Tuple
# value = (10,20)
# print(f"{value}")
# print(f"{value[0],value[1]}")

#===Ex-28=== Dictionary
# data = {'Aqib':2000, 'Zaman':5000}
# print(f"{data['Aqib']:d} {data['Zaman']:d}")
#
# #===Ex-28=== function
# name = "Incis"
# print(f"{name.upper()}")
# print(f"{name.lower()}")
#
# print(f"{{10}}")

# #===Ex-29=== date-time
#
# from datetime import datetime
#
# today = datetime(2020,11,30)
# print(f"{today}") #default format
# print(f"{today:%d-%B-%y}")
# print(f"{today:%d/%m/%Y}")

