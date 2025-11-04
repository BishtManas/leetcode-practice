class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root):
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)
        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    if first and second:
        first.val, second.val = second.val, first.val


# Helper to build tree from list (like LeetCode)
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


# Helper for inorder print
def inorder_print(root):
    if not root:
        return []
    return inorder_print(root.left) + [root.val] + inorder_print(root.right)


# -------- Example Runs --------
root1 = build_tree([1, 3, None, None, 2])
print("Before:", inorder_print(root1))
recoverTree(root1)
print("After:", inorder_print(root1))
# Expected inorder output should be sorted

root2 = build_tree([3, 1, 4, None, None, 2])
print("Before:", inorder_print(root2))
recoverTree(root2)
print("After:", inorder_print(root2))
