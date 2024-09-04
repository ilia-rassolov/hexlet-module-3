class Node:
    acc = None
    value = None

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        # self.acc = []

    def to_list(self):
        i = next(self)
        return i

    def __next__(self):
        if not self.key:
            pass
        # for i in range(3):
        #     yield i

        yield self
        for x in (self.left, self.right):
            if x:
                yield x.__next__()


# def len(self):
#     # self.acc = 0
#     print(f"{self.key=}")
#     if not self.key:
#         pass
#     self.acc += 1
#     if self.left:
#         current_value = len(self.left.key)
#         self.acc += current_value
#     elif self.right:
#         self.acc += len(self.left.key)
#     return self.acc


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
# tree = Node(5, Node(2, left=Node(1, right=Node(6)), right=Node(4)))
# print((len(tree)))  # 9
# print(tree.total())  # 97
print(tree.to_list())  # [9, 4, 8, 6, 3, 7, 17, 22, 20]
# tree.every(lambda key: key <= 22)  # True
# tree.some(lambda key: key > 22)  # False
# tree.minimum()  # 3
# tree.maximum()  # 22
# tree2 = Node(3, Node(1), Node(2))
# tree2  # выводится repr(tree2)
# # Node(3, Node(1, None, None), Node(2, None, None))
