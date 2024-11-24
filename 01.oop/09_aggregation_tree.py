class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return self

    def to_list(self):
        self.acc = [self.key]
        if self.left:
            acc_left = self.left.to_list()
            self.acc.extend(acc_left)
        if self.right:
            acc_right = self.right.to_list()
            self.acc.extend(acc_right)
        return self.acc

    def __len__(self):
        return len(self.to_list())

    def total(self):
        return sum(self.to_list())

    def minimum(self):
        return min(self.to_list())

    def maximum(self):
        return max(self.to_list())

    def every(self, fn):
        return sum(map(fn, self.to_list())) == len(self.to_list())

    def some(self, fn):
        return sum(map(fn, self.to_list())) > 0

tree = Node(
    10,
    Node(
        4,
        Node(8),
        Node(
            6,
            Node(3),
            Node(7),
        ),
    ),
    Node(
        17,
        right=Node(
            22,
            Node(20),
        ),
    ),
)

print(tree.to_list())
print(tree.__len__())
print(tree.total())
print(tree.minimum())
print(tree.maximum())
print(tree.every(lambda key: key <= 20))
print(tree.some(lambda key: key <= 20))
print(tree.__repr__())

# tree2  # выводится repr(tree2)
# # Node(3, Node(1, None, None), Node(2, None, None))
