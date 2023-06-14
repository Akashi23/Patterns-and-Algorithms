from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        queue = []
        current = sum([x for x in nums[:k]])
        queue.append(current)

        if k == length:
            return current / k

        for i in range(k, length):
            current = current + nums[i] - nums[i - k]
            queue.append(current)

        return max(queue) / k


solution = Solution()
answer = solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print(answer)
assert answer == 12.75

answer = solution.findMaxAverage([5], 1)
print(answer)
assert answer == 5

answer = solution.findMaxAverage([0, 1, 1, 3, 3], 4)
print(answer)
assert answer == 2

answer = solution.findMaxAverage([0, 4, 0, 3, 2], 1)
print(answer)
assert answer == 4

answer = solution.findMaxAverage([9, 7, 3, 5, 6, 2, 0, 8, 1, 9], 6)
print(answer)
assert answer == 5.333333333333333
