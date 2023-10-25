class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: TreeNode) -> int:
    if root is None:
        return 0

    stack = [(root, 0)]
    d = 0

    while stack:
        node, depth = stack.pop()
        d += depth

        if node.left:
            stack.append((node.left, depth + 1))

        if node.right:
            stack.append((node.right, depth + 1))

    return d


    # def sum(node, depth):
    #     if node is None:
    #         return 0
    #     return depth + sum(node.left, depth + 1) + sum(node.right, depth + 1)
    #
    # return sum(root, 0)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.left.right.right.left = TreeNode(8)
root.left.right.right.right = TreeNode(9)
result = sum_of_depths(root)
print(result)
