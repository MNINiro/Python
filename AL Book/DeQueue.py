# Deque Vs. Queue
# Queue is an abstract data structure which keeps an order of
# elements in it. We can add element to the end of a sequence
# and remove element from the head of the sequence in a queue.
# Queue can be referred as FIFO (First in First out). This means
# retrieving elements from a queue happens in the same order as
# they were put in it.

# Deque or dequeue is double-ended queue. We can add and remove
# elements to and from both ends of a sequence.

# Both Queue and Deque does not specify access to elements between
# their ends. So, implementation of queue or dequeue may or may not
# provide operations for accessing elements others than current ends
# of the sequence. Also Queue and Deque may provide such operations
# with a very different efficiency.

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)
