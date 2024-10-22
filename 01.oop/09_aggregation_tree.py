class Node:
    acc = None
    value = None

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.acc = []

    # def __repr__(self):
    #     return



    def __next__(self):
        # if not self.key:
        #     pass
        yield self
        if self.left:
            yield self.left.__next__()
        if self.right:
            yield self.right.__next__()

    # def __iter__(self):
    #     yield self
    #     if self.left:
    #         yield self.left
    #         yield self.left.__iter__()
    #     if self.right:
    #         yield self.right
    #         yield self.right.__iter__()
    #
    # def to_list(self):
    #     I = self
    #     return list(next(self))

    def to_list(self):
        if not self.key:
            pass
        self.acc.append(self.key)
        if self.left:
            acc_left = self.left.to_list()
            self.acc.extend(acc_left)
        if self.right:
            acc_right = self.right.to_list()
            self.acc.extend(acc_right)
        return self.acc

    # def __len__(self):
    #     return sum(map(lambda x: 1, self.acc))


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


print(tree.to_list())  # [9, 4, 8, 6, 3, 7, 17, 22, 20]
# print((len(tree)))  # 9
# print(tree.total())  # 97

# tree.every(lambda key: key <= 22)  # True
# tree.some(lambda key: key > 22)  # False
# tree.minimum()  # 3
# tree.maximum()  # 22
# tree2 = Node(3, Node(1), Node(2))
# tree2  # выводится repr(tree2)
# # Node(3, Node(1, None, None), Node(2, None, None))
