from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return reduce(
            lambda count, value: count + (value * (value - 1)) // 2,
            Counter(nums).values(),
            0,
        )


solution = Solution()
answer = solution.numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(answer)
assert answer == 4

answer = solution.numIdenticalPairs([1, 1, 1, 1])
print(answer)
assert answer == 6

answer = solution.numIdenticalPairs([1, 2, 3])
print(answer)
assert answer == 0

answer = solution.numIdenticalPairs([1, 1, 1, 1, 1])
print(answer)
assert answer == 10
