# 1441. Build an Array With Stack Operations
class Solution:
    def buildArray(self, target, n):
        result = []
        current = 1
        for num in target:
            while current < num:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1
        return result

# 1209. Remove All Adjacent Duplicates in String II 
class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()
        return "".join(
            char * count for char, count in stack
        )    

