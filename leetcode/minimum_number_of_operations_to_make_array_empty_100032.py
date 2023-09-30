from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        c = Counter(nums)
        op = 0

        for i in c:
            if c[i] == 1:
                return -1
            op += (c[i] + 2) // 3
        return op
    

solution = Solution()
answer = solution.minOperations([2,3,3,2,2,4,2,3,4])
print(answer)
assert answer == 4

answer = solution.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12])
print(answer)
assert answer == 7