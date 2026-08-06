# 933. Number of Recent Calls
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
from collections import deque
class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# 752. Open the Lock
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
# Each move consists of turning one wheel one slot.
from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for i in range(4):
                digit = int(lock[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    new_lock = lock[:i] + str(new_digit) + lock[i+1:]
                    if new_lock not in dead and new_lock not in visited:
                        visited.add(new_lock)
                        q.append((new_lock, steps + 1))
        return -1
      
