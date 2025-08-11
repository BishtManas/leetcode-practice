# Standalone ListNode class for VS Code
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Helper function to create linked list from Python list
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print linked list as Python list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: [7, 0, 8]