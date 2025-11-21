class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)  # start of sorted list
        curr = head         # current node we want to insert
        
        while curr:
            next_node = curr.next  # save next before altering pointers
            
            # find the correct place to insert curr
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node  # move to next node in original list
        
        return dummy.next
