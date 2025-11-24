class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return root
    
    leftmost = root

    while leftmost.left:
        head = leftmost

        while head:
            head.left.next = head.right

            if head.next:
                head.right.next = head.next.left

            head = head.next

        leftmost = leftmost.left

    return root


# Helper to print level-by-level using next pointers
def print_levels(root):
    level_start = root
    while level_start:
        cur = level_start
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")
        level_start = level_start.left


# Example tree: [1,2,3,4,5,6,7]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connect(root)
print_levels(root)
