class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build_trees(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end + 1):
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees

        return build_trees(1, n)

# Helper function to print the tree as list
def serialize(root):
    if not root:
        return None
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner look
    while result and result[-1] is None:
        result.pop()
    return result

# Run the program
if __name__ == "__main__":
    n = 3
    sol = Solution()
    trees = sol.generateTrees(n)
    print(f"Total Trees for n={n}: {len(trees)}")
    for t in trees:
        print(serialize(t))
