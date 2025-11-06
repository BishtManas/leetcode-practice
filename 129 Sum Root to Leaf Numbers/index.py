from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None

    nodes = [None if v is None else TreeNode(v) for v in arr]
    kid = 1

    for i in range(len(arr)):
        if nodes[i] is not None:
            if kid < len(arr):
                nodes[i].left = nodes[kid]
                kid += 1
            if kid < len(arr):
                nodes[i].right = nodes[kid]
                kid += 1

    return nodes[0]

def sum_root_to_leaf(root):
    def dfs(node, curr):
        if not node:
            return 0
        curr = curr * 10 + node.val
        if not node.left and not node.right:
            return curr
        return dfs(node.left, curr) + dfs(node.right, curr)

    return dfs(root, 0)

# Test in VS Code
if __name__ == "__main__":
    arr = [4, 9, 0, 5, 1]
    root = build_tree(arr)
    print(sum_root_to_leaf(root))  # Expected: 1026
