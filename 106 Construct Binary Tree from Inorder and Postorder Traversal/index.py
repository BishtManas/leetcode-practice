# LeetCode-ready solution

class Solution:
    def buildTree(self, inorder, postorder):
        # Map value -> index in inorder for O(1) lookup
        index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Postorder pointer (last index)
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            # No elements to build
            if left > right:
                return None

            # Last element in postorder is the root
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Get the inorder position
            mid = index_map[root_val]

            # Build RIGHT subtree first (important!)
            root.right = helper(mid + 1, right)
            # Build LEFT subtree
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
