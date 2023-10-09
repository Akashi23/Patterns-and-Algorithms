import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


solution = Solution()
answer = solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(answer)
assert answer == 5

answer = solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
print(answer)
assert answer == 4
