class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def initializeBinaryTree() -> BinaryTreeNode:
    a = BinaryTreeNode(2)
    b = BinaryTreeNode(3)
    c = BinaryTreeNode(1, a, b)
    return c
