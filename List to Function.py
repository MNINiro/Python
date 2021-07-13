#=== Passing a List to a function
y = [];
def show(lt):
    print(lt)
    print(type(lt))
    for i in lt:
       y.append(i*2)
       print(y)
    return y

lst = [10,34,65,23,77]
x = show(lst)
print()
print(x)
print(type(x))


