# Ex-1
import mymodule

n = mymodule.person1["name"]
print(n)

a = mymodule.person2["age"]
print(a)

c = mymodule.person3["country"]
print(c)

def greeting(name):
  print("Hello, " + name)

greeting(n)


# Ex-2
import platform

x = platform.system()
print(x)

# Ex-3
x = dir(platform)
print(x)

# Ex-3
# import json
#
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])