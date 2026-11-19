# 147. Insertion Sort List
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            next_node = curr.next
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
        return dummy.next 

# 868. Binary Gap
class Solution:
    def binaryGap(self, n):
        last_position = -1
        result = 0
        position = 0
        while n > 0:
            if n & 1:
                if last_position != -1:
                    result = max(result, position - last_position)
                last_position = position
            n >>= 1
            position += 1
        return result   
