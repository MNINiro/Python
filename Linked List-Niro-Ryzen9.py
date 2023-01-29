# A linked list is created by using the node class we studied in the last chapter.
# We create a Node object and create another class to use this ode object.
# We pass the appropriate values through the node object to point to the
# next data elements. The below program creates the linked list with three
# data elements. In the next section we will see how to traverse the linked list.

# ===========Creation of Linked list=======================
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None


lst = SLinkedList()       # lst is an object/instance of SLinkedList() class
lst.headval = Node("Mon")
e2 = Node("Tue")            # e2 and e3 are the objects/instances of node() class
e3 = Node("Wed")

# Link first Node to second node
lst.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
"""

"""
# ==============Traversing a Linked List=====================
# Single linked lists can be traversed in only forward direction starting form
# the first data element. We simply print the value of the next data element by
# assigning the pointer of the next node to the current data element.

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


lst = SLinkedList()
lst.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
lst.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

lst.listprint()


"""
# =====================Inserting at the Beginning========================================
# Inserting element in the linked list involves reassigning the pointers from
# the existing nodes to the newly inserted node. Depending on whether the new
# data element is getting inserted at the beginning or at the middle or at the
# end of the linked list, we have the below scenarios.

# Inserting at the Beginning
# This involves pointing the next pointer of the new data node to the current
# head of the linked list. So the current head of the linked list becomes the
# second data element and the new node becomes the head of the linked list.

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headVal = None

    # Print the linked list

    def listprint(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataval)
            printVal = printVal.nextval

    def atBegining(self, newdata):
        NewNode = Node(newdata)

        # Update the new nodes next val to existing node
        NewNode.nextval = self.headVal
        self.headVal = NewNode


lst = SLinkedList()
lst.headVal = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

lst.headVal.nextval = e2
e2.nextval = e3

lst.atBegining("Sun")   # first insert the new data atBigining class method
lst.listprint()
"""
"""
# ===================Inserting at the End==========================================
# This involves pointing the next pointer of the current last node of
# the linked list to the new data node. So the current last node of the
# linked list becomes the second last data node and the new node becomes
# the last node of the linked list.

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        # print("New Node:", NewNode.dataval)
        if self.headval is None:
            self.headval = NewNode
            # print("Test:", self.headval)
            return
        last = self.headval
        while last.nextval:         #This loop will run until it reaches the last element
            last = last.nextval
        last.nextval = NewNode

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


lst = SLinkedList()
lst.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

lst.headval.nextval = e2
e2.nextval = e3

lst.AtEnd("Thu")

lst.listprint()
"""

# ==============Inserting in between two Data Nodes==============================
# This involves changing the pointer of a specific node to point to the new node.
# That is possible by passing in both the new node and the existing node after
# which the new node will be inserted. So we define an additional class which
# will change the next pointer of the new node to the next pointer of middle node.
# Then assign the new node to next pointer of the middle node.
"""


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Function to add node
    def Inbetween(self, middle_node, newdata):
        # print("Middle node:", middle_node.dataval)
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


lst = SLinkedList()
lst.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

lst.headval.nextval = e2
e2.nextval = e3
# print("lst.headval.nextval", lst.headval.nextval.dataval)
lst.Inbetween(lst.headval.nextval, "Fri")

lst.listprint()
"""

# ==============Removing an Item===============================
# We can remove an existing node using the key for that node.
# In the below program we locate the previous node of the node
# which is to be deleted.Then, point the next pointer of this node
# to the next node of the node to be deleted.
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    # Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.data == Removekey:
                self.head = HeadVal.next
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if HeadVal is None:
            return

        prev.next = HeadVal.next
        HeadVal = None

    def LListprint(self):
        printval = self.head
        while printval:
            print(printval.data),
            printval = printval.next


llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()
"""
