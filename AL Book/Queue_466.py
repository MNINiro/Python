# queue = [None for index in range(0, 10)]
queue = []
frontPointer = 0
rearPointer = -1
queueFull = 5
queueLength = 0


def enQueue(item):
    global queueLength, rearPointer

    if queueLength < queueFull:
        print(queueLength, ' ', queueFull)

        if rearPointer < len(queue) - 1:     #initially before append
            rearPointer = rearPointer + 1
            print('Length:', len(queue) - 1)
            print('rearPointer:', rearPointer)
        else:
            rearPointer = 0
            queueLength = queueLength + 1
            queue.append(item)            # queue[rearPointer] = item

            print('Rear Pointer:', rearPointer)
            print('queueLength:', queueLength)
            print(queue)

    else:
        print("Queue is full, cannot enqueue")

# =======================================================
def deQueue():
    global queueLength, frontPointer, item
    if queueLength == 0:
        print("Queue is empty,cannot dequeue")
    else:
        item = queue[frontPointer]
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
    queueLength = queueLength -1


# ============= Main Body ===================
for i in range(10):
    data = int(input('Enter data:'))
    enQueue(data)

print(queue)
