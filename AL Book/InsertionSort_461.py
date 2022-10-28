"""
DECLARE myList : ARRAY[0:8] OF INTEGER
DECLARE upperBound : INTEGER
DECLARE lowerBound : INTEGER
DECLARE index : INTEGER
DECLARE key : BOOLEAN
DECLARE place : INTEGER
"""


def insertionSort(myList):
    lowerBound = 0
    upperBound = len(myList)
    print('Initial list:', myList)

    for index in range(lowerBound + 1, upperBound):
        print('index:', index)

        key = myList[index]
        print("Key :", key)

        place = index - 1
        print('Place:', place)

        while place >= lowerBound and myList[place] > key:
            print('myList[place]:', myList[place])

            temp = myList[place + 1]
            print('myList[place + 1]:', myList[place + 1])
            print('temp:', temp)

            myList[place + 1] = myList[place]
            print('myList[place + 1]:', myList[place + 1])

            myList[place] = temp
            print('myList[place]:', myList[place])

            place = place - 1
            print("place :", place)

        myList[place + 1] = key
        print("myList[place] :", myList[place + 1])
        print("place:", place)
        print(myList)
        print("")


myList = [85, 12, 59, 45, 72, 51]
insertionSort(myList)
print(myList)
