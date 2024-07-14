class Node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, value):
        if self.key is None:
            self.key = value
            return self.__class__(value)
        elif self.key == value:
            pass
        elif self.key < value:
            if self.right is None:
                self.right = self.__class__(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = self.__class__(value)
            else:
                self.left.insert(value)
        return self



root = Node()
root.insert(50)
root.insert(50)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)
# root.insert(100)

print(root.key)
print(root.left.key)
print(root.right.key)
print(root.right.right.key)
print(root.right.right.right)
