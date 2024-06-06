class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key




def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
        return root




def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)





root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)


print(root.left.left.val)
# tree.insert(8)
# tree.insert(17)
# tree.insert(4)
# tree.insert(3)
# tree.insert(6)
# print(f"{tree.key=}")
# print(f"{tree.left.key=}")
# print(f"{tree.right.key=}")
# print(f"{tree.left.left.key=}")
# print(f"{tree.left.right.key=}")