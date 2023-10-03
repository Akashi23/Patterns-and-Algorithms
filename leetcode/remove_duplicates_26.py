from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = list(dict.fromkeys(nums))
        for i in range(len(s)):
            nums[i] = s[i]
        return len(s)


solution = Solution()
answer = solution.removeDuplicates([1, 1, 2])
print(answer)
assert answer == 2

answer = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(answer)
assert answer == 5
