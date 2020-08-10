numbers = [5,4,9,10,2,8]

def bubblesort(numbers):
    for i in range (len(numbers)):

        for j in range(len(numbers)-i-1):
            if numbers[j]>numbers[j+1]:

                temp=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp
##                print(numbers)

bubblesort(numbers)
print(numbers)
lowest=numbers[0]
x=len(numbers)
highest=numbers[x-1]

print('lowest is:',lowest)
print('highest is :',highest)
