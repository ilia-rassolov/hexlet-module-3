class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def search(self, key):
        if key == self.key:
            return self
        if key < self.key:
            if self.left:
                return self.left.search(key)
            return None
        else:
            if self.right:
                return self.right.search(key)
            return None


node5 = Node(5)
node22 = Node(22, left=Node(20))
tree = Node(
    9,
    Node(
        4,
        Node(3),
        Node(
            6,
            node5,
            Node(7),
        ),
    ),
    Node(
        17,
        right=node22,
    ),
)

print(tree.search(4))  # 6
print(tree.search(6).left.key)# 5
print(tree.search(6).right.key)  # 7
print(tree.search(5) is node5)  # True
print(tree.left.left.key)  # 3
print(Node(3))
