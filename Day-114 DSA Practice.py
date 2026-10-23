# 941. Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
class Solution:
    def validMountainArray(self, arr):
        i, n = 0, len(arr)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1

# 2095. Delete the Middle Node of a Linked List
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
      
