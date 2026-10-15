# 832. Flipping an Image
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image

# 120. Triangle
# Given a triangle array, return the minimum path sum from top to bottom.
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
      
