class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __len__(self, acc=1):
        if not self.key:
            return 0
        acc += 1
        print(f"{acc=}")
        for node in (self.left, self.right):
            if node is None:
                print('Hi from left!')
                print(f"{acc}=")
                acc += 1
                return node.__len__(acc)
        return acc



tree = Node(
    9,
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
tree = Node(5, Node(2), Node(6, Node(4)))
print(len(tree))  # 9
# tree.total()  # 96
# tree.to_list()  # [9, 4, 8, 6, 3, 7, 17, 22, 20]
# tree.every(lambda key: key <= 22)  # True
# tree.some(lambda key: key > 22)  # False
# tree.minimum()  # 3
# tree.maximum()  # 22
# tree2 = Node(3, Node(1), Node(2))
# tree2  # выводится repr(tree2)
# # Node(3, Node(1, None, None), Node(2, None, None))