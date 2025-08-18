from collections import deque

# Tree Node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        # Swap left and right
        root.left, root.right = root.right, root.left
        
        # Recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Function to build a tree from list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Function to print tree in level order
def print_tree(root):
    if not root:
        print([])
        return
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    print(result)

# Example usage:
values = [4, 2, 7, 1, 3, 6, 9]  # Original tree
root = build_tree(values)

print("Original Tree:")
print_tree(root)

solution = Solution()
inverted_root = solution.invertTree(root)

print("Inverted Tree:")
print_tree(inverted_root)