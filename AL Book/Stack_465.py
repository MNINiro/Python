def pushStack(stack, item):
    topPointer = 5          #increase/decrease topPointer value to examine the code
    stackFull = 6
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        # stack[topPointer] = item
        stack.append(item)
    else:
        print("Stack is full, cannot push")
    print(stack)


def popStack(stack):
    topPointer = 5
    basePointer = 0
    if topPointer == basePointer - 1:
        print("Stack is empty,cannot pop")
    else:
        # item = stack[topPointer]
        stack.pop()
        topPointer = topPointer - 1
    print(stack)


stack = [10, 25, 19, 75, 5]
pushStack(stack, 55)
popStack(stack)
