from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        


solution = Solution()
answer = solution.longestSubarray([1, 1, 0, 1])
print(answer)
assert answer == 3

answer = solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])
print(answer)
assert answer == 5

answer = solution.longestSubarray([1, 1, 1])
print(answer)
assert answer == 2

answer = solution.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1])
print(answer)
assert answer == 4

answer = solution.longestSubarray([0, 0, 0])
print(answer)
assert answer == 0

answer = solution.longestSubarray([0, 0, 1, 1])
print(answer)
assert answer == 2

answer = solution.longestSubarray([])
print(answer)
assert answer == 0

answer = solution.longestSubarray(
    [
        1,
        1,
        1,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
    ]
)
print(answer)
assert answer == 18
