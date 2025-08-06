class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# Helper function to create a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node if cycle_node else head

    return head

# 🔄 Example test case
values = [3, 2, 0, -4]
pos = 1  # cycle starts at node with value 2
head = create_linked_list_with_cycle(values, pos)

# ✅ Test the function
sol = Solution()
print("Cycle Detected:" if sol.hasCycle(head) else "No Cycle Found")
# True for Cycle Detected and False for No cycle found.
