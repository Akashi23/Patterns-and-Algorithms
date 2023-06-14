from typing import List
import heapq


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return heapq.nlargest(1, prices)[0] - heapq.nsmallest(1, prices)[0]


solution = Solution()
answer = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(answer)
assert answer == 5
