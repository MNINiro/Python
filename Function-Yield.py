# #===Ex-1===
# def disp(a,b):
#     yield a
#     yield b
#
# # x,y = disp(10,20)
# # print(x)
# # print(y)
#
# result = disp(10,20)
# print(result)       #will print only memory locations
# print(type(result)) #generator object will return
# print(next(result)) #generate first value
# print(next(result)) #generate next value

#===Ex-2===
def show(a,b):
    while a <= b:
        yield a
        a += 1
result = show(1,3)
# print(next(result))
# print(next(result))
# print(next(result))

for i in range(3):
    print(next(result))