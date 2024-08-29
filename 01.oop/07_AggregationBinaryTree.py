class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.count = 0

    def walk(self, func):
        if self.left is None and self.right is None:
            return func(self.key)
        print(f"{self=}")
        children = list(filter(lambda x: x is not None, [self.left, self.right]))
        print(f"{children=}")
        descendant_counts = list(map(walk(func), children))
        return func(self.key) + sum(descendant_counts)

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
# tree.len()
# print(len(tree))
print(f"{tree.count=}")  # 9


