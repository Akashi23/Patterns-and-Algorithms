from math import inf
from typing import List
from heapq import nlargest, nsmallest

#The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k]
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix = []
        mx = -inf

        for n in nums:
            mx = max(mx, n)
            prefix.append(max(mx-n, 0))

        suffix = []
        for n in reversed(nums):
            suffix.append(n if not suffix else max(suffix[-1], n))
        suffix[:] = reversed(suffix)
        return max(prefix[i]*suffix[i+1] for i in range(len(nums) - 1))

solution = Solution()
answer = solution.maximumTripletValue([12,6,1,2,7])
print(answer)
assert answer == 77

answer = solution.maximumTripletValue([1,10,3,4,19])
print(answer)
assert answer == 133

answer = solution.maximumTripletValue([1,2,3])
print(answer)
assert answer == 0

answer = solution.maximumTripletValue([2,3,1])
print(answer)
assert answer == 0