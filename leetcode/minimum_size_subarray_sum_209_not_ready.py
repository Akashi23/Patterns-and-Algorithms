from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


solution = Solution()
answer = solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(answer)
assert answer == 2
