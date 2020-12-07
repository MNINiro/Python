#=== Passing a List to a function
def show(lt):
    print(lt)
    print(type(lt))
    for i in lt:
        print(i)
    return lt

lst = [10,34,65,23,77]
# show(lst)

lst1 = show(lst)
print(lst1)
print(type(lst1))


