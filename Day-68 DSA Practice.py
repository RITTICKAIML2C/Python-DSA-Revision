# 406. Queue Reconstruction by Height
# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). 
# Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            result.insert(person[1], person)
        return result

# 455. Assign Cookies
# Assume you are an awesome parent and want to give your children some cookies. 
# But, you should give each child at most one cookie.
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child
