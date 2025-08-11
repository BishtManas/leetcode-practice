# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

# Helper function to print the tree in level order
from collections import deque
def print_tree(root):
    if not root:
        print("[]")
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

# Example usage
solution = Solution()
nums = [-10, -3, 0, 5, 9]
tree_root = solution.sortedArrayToBST(nums)
print_tree(tree_root)