class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def helper(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root)


# Helper function to build tree from list (like LeetCode input)
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


# -------- Example Runs --------
root1 = build_tree([2, 1, 3])
print(isValidBST(root1))  # Expected: True

root2 = build_tree([5, 1, 4, None, None, 3, 6])
print(isValidBST(root2))  # Expected: False
