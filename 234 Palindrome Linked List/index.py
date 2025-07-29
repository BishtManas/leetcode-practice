class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare both halves
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

# 🔧 Helper function to create linked list from Python list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# ✅ Test the code
if __name__ == "__main__":
    test_list = [1, 2, 2, 1]   # Change this list to test other inputs
    head = create_linked_list(test_list)
    sol = Solution()
    print("Is Palindrome:", sol.isPalindrome(head))
