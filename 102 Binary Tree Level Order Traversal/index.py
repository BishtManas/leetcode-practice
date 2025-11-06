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
    kid_index = 1

    for i in range(len(arr)):
        if nodes[i] is not None:
            if kid_index < len(arr):
                nodes[i].left = nodes[kid_index]
                kid_index += 1
            if kid_index < len(arr):
                nodes[i].right = nodes[kid_index]
                kid_index += 1

    return nodes[0]

def level_order(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result


# Test it in VS Code
if __name__ == "__main__":
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree(arr)
    print(level_order(root))
