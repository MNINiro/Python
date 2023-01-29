class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    # Add integer to binary tree
    def insert(self, item):
        if self.item:
            if item < self.item:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item

    # Search for integer in binary tree
    def search(self, item):
        while self.item != item:
            if item < self.item:
                self.item = self.left
            else:
                self.item = self.right

            if self.item is None:
                return None
        return self.item


tree = Node(27)

tree.insert(55)
tree.insert(66)
tree.insert(45)

tree.search(55)
