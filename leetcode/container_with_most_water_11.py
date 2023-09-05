from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(currentArea, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


solution = Solution()
answer = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(answer)
assert answer == 49

answer = solution.maxArea([1, 1])
print(answer)
assert answer == 1

answer = solution.maxArea([4, 3, 2, 1, 4])
print(answer)
assert answer == 16

answer = solution.maxArea([1, 2, 1])
print(answer)
assert answer == 2

answer = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 25, 7])
print(answer)
assert answer == 49

answer = solution.maxArea([8, 20, 1, 2, 3, 4, 5, 6])
print(answer)
assert answer == 42
