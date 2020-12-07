#=== Ex-1 ===Replace
str1 = "Hi dear"
old = "Hi"
new = "Hello"
output = str1.replace(old,new)
print(output)

#=== Ex-2 ===
str2 = "Gentleman"
print(str2.replace("man","woman"))

#=== Ex-3 ===Split
msg = "how are you doing?"
print(msg.split(' '))

#=== Ex-4 ===
msg = "how-are-you-doing?"
print(msg.split('-'))

#=== Ex-5 ===join
str3 = ('Hello', 'how', 'are', 'you')
print(str3)
out = ' '.join(str3)
print(out)
out = '-'.join(str3)
print(out)
