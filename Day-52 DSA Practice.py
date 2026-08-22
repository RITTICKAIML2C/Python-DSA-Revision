# 160. Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# The functions get and put must each run in O(1) average time complexity.
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))
