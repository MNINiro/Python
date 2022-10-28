text = input("Enter a palindromic string:")
lst = list(text)
print(lst)
ln = len(lst)
mid = ln//2
pal = False

for i in range(ln):
    if lst[i] == lst[ln-i-1]:
        pal = True
        if i == mid:
            break
    else:
        pal = False

if pal:
    print("It's a palindrome")

