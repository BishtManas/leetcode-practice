# -----------------------------
# Binary Tree Zigzag Traversal
# Standalone VS Code version
# -----------------------------

from collections import deque

# Define the tree node structure
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to build a tree from list input
def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Zigzag level order traversal
def zigzagLevelOrder(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level_nodes.reverse()

        result.append(level_nodes)
        left_to_right = not left_to_right

    return result

# -----------------------------
# Example usage (edit this)
# -----------------------------
# Just change this list to test any tree
input_tree = [3, 9, 20, None, None, 15, 7]

root = build_tree(input_tree)
output = zigzagLevelOrder(root)

print("Input tree:", input_tree)
print("Zigzag Output:", output)
