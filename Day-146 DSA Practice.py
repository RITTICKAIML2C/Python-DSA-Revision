# 1287. Element Appearing More Than 25% In Sorted Array
class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr)
        threshold = n // 4
        for i in range(n - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]
        return -1

# 1861. Rotating the Box
class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        # Step 1: Apply gravity to each row
        for row in box:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j] = '.'
                    row[empty] = '#'
                    empty -= 1
        # Step 2: Rotate the box 90 degrees clockwise
        result = []
        for j in range(n):
            new_row = []
            for i in range(m - 1, -1, -1):
                new_row.append(box[i][j])
            result.append(new_row)
        return result
