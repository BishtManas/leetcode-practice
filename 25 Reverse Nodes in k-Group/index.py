# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(ll):
            previous = None
            node = ll
            while node:
                next_node = node.next
                node.next = previous
                previous = node
                node = next_node
            return previous

        def length(ll):
            curr = ll
            n = 0
            while curr:
                curr = curr.next
                n += 1
            return n

        ln = length(head)

        initial = ListNode(None)
        initial.next = head
        start = initial

        for _ in range(ln // k):
            curr = start

            # move k steps ahead
            for _ in range(k):
                curr = curr.next

            ahead = curr.next
            curr.next = None

            toDo = start.next
            start.next = None

            # reverse current group
            last = reverse(toDo)

            # reconnect
            toDo.next = ahead
            start.next = last

            # move start pointer
            start = toDo

        return initial.next