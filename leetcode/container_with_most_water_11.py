from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        



solution = Solution()
answer = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(answer)
assert answer == 49

answer = solution.maxArea([1,1])
print(answer)
assert answer == 1

answer = solution.maxArea([4,3,2,1,4])
print(answer)
assert answer == 16
