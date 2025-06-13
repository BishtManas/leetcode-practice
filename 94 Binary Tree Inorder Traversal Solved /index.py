from typing import Optional, List

# Define the structure of each node in the tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Value of the node
        self.left = left      # Left child (TreeNode)
        self.right = right    # Right child (TreeNode)

# Your solution with inorder traversal (iterative)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left 

            current = stack.pop()
            answer.append(current.val)
            current = current.right

        return answer

# ------------------------------
# Create the tree: [1, null, 2, 3]
# Tree structure:
#     1
#      \
#       2
#      /
#     3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create an object of Solution and call the function
sol = Solution()
result = sol.inorderTraversal(root)

# Print the output
print("Inorder Traversal:", result)
